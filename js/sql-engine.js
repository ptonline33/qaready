/* QAReady mini SQL engine.
 *
 * A tiny, dependency-free SQL interpreter so learners can actually RUN the
 * queries in the "SQL for Testers" course, fully offline. It intentionally
 * supports the useful teaching subset rather than full SQL:
 *
 *   SELECT [DISTINCT] cols | * | COUNT/SUM/AVG/MIN/MAX(...) [AS alias]
 *   FROM table [AS alias]
 *   [JOIN table [AS alias] ON condition]*
 *   [WHERE condition]
 *   [GROUP BY columns]
 *   [HAVING condition]
 *   [ORDER BY column [ASC|DESC]]
 *   [LIMIT n]
 *
 * Conditions: AND / OR / NOT, parentheses, = != < > <= >=, LIKE 'pat%',
 * IN (...), BETWEEN a AND b, IS [NOT] NULL, NOT IN, NOT LIKE.
 *
 * Ported and extended from the DeskReady exercise engine. Everything here is
 * deterministic and side-effect free; writes are taught conceptually, not run.
 */
const SQL = (() => {
  "use strict";

  const AGGS = new Set(["COUNT", "SUM", "AVG", "MIN", "MAX"]);

  function tokenize(sql) {
    const toks = [];
    let i = 0;
    while (i < sql.length) {
      const c = sql[i];
      if (/\s/.test(c)) { i++; continue; }
      if (c === ";") { i++; continue; }
      if (c === "'") {
        let j = i + 1, s = "";
        while (j < sql.length) {
          if (sql[j] === "'" && sql[j + 1] === "'") { s += "'"; j += 2; continue; }
          if (sql[j] === "'") break;
          s += sql[j++];
        }
        if (j >= sql.length) throw new Error("A text value is missing its closing quote.");
        toks.push({ t: "str", v: s });
        i = j + 1;
        continue;
      }
      if (/[0-9]/.test(c) || (c === "-" && /[0-9]/.test(sql[i + 1] || ""))) {
        let j = i, s = "";
        if (sql[j] === "-") { s += "-"; j++; }
        while (j < sql.length && /[0-9.]/.test(sql[j])) s += sql[j++];
        toks.push({ t: "num", v: parseFloat(s) });
        i = j;
        continue;
      }
      if (/[A-Za-z_]/.test(c)) {
        let j = i, s = "";
        while (j < sql.length && /[A-Za-z0-9_.]/.test(sql[j])) s += sql[j++];
        toks.push({ t: "id", v: s });
        i = j;
        continue;
      }
      const two = sql.slice(i, i + 2);
      if (two === ">=" || two === "<=" || two === "!=" || two === "<>") {
        toks.push({ t: "op", v: two === "<>" ? "!=" : two });
        i += 2;
        continue;
      }
      if (c === "=" || c === "<" || c === ">") { toks.push({ t: "op", v: c }); i++; continue; }
      if (c === "(") { toks.push({ t: "lp" }); i++; continue; }
      if (c === ")") { toks.push({ t: "rp" }); i++; continue; }
      if (c === ",") { toks.push({ t: "comma" }); i++; continue; }
      if (c === "*") { toks.push({ t: "star" }); i++; continue; }
      throw new Error(`I don't understand the character "${c}".`);
    }
    return toks;
  }

  function parse(sql) {
    const toks = tokenize(sql);
    let p = 0;
    const peek = (k = 0) => toks[p + k];
    const atKw = (w, k = 0) => {
      const t = toks[p + k];
      return !!t && t.t === "id" && t.v.toUpperCase() === w;
    };
    const eatKw = (w) => { if (!atKw(w)) throw new Error(`Expected the keyword ${w}.`); p++; };
    const next = () => toks[p++];
    const expect = (t, what) => {
      const tok = next();
      if (!tok || tok.t !== t) throw new Error(`Expected ${what}.`);
      return tok;
    };
    const maybeAlias = () => (atKw("AS") ? (p++, expect("id", "an alias").v) : null);

    /* ---- SELECT list ---- */
    eatKw("SELECT");
    let distinct = false;
    if (atKw("DISTINCT")) { distinct = true; p++; }
    const select = [];
    for (;;) {
      let item;
      if (peek() && peek().t === "star") {
        next();
        item = { kind: "star" };
      } else {
        const name = expect("id", "a column name").v;
        if (peek() && peek().t === "lp") {
          next();
          const fn = name.toUpperCase();
          if (!AGGS.has(fn)) throw new Error(`${name}() is not a function I support here.`);
          let arg = "*";
          if (peek() && peek().t === "star") next();
          else if (peek() && peek().t === "id") arg = next().v;
          expect("rp", "a closing parenthesis");
          item = { kind: "agg", fn, arg };
        } else {
          item = { kind: "col", name };
        }
      }
      item.alias = maybeAlias();
      select.push(item);
      if (peek() && peek().t === "comma") { next(); continue; }
      break;
    }

    /* ---- FROM + JOINs ---- */
    eatKw("FROM");
    const from = expect("id", "a table name").v;
    const fromAlias = maybeAlias();
    const joins = [];
    while (atKw("JOIN") || atKw("INNER")) {
      if (atKw("INNER")) p++;
      p++; // JOIN
      const table = expect("id", "a table name after JOIN").v;
      const alias = maybeAlias();
      eatKw("ON");
      joins.push({ table, alias, on: parseOr() });
    }

    let where = null;
    if (atKw("WHERE")) { p++; where = parseOr(); }
    let groupBy = null;
    if (atKw("GROUP")) {
      p++; eatKw("BY");
      groupBy = [expect("id", "a column after GROUP BY").v];
      while (peek() && peek().t === "comma") { p++; groupBy.push(expect("id", "another GROUP BY column").v); }
    }
    let having = null;
    if (atKw("HAVING")) { p++; having = parseOr(); }
    let orderBy = null;
    if (atKw("ORDER")) {
      p++; eatKw("BY");
      const col = expect("id", "a column after ORDER BY").v;
      let dir = "ASC";
      if (atKw("ASC") || atKw("DESC")) dir = next().v.toUpperCase();
      orderBy = { col, dir };
    }
    let limit = null;
    if (atKw("LIMIT")) { p++; limit = expect("num", "a number after LIMIT").v; }
    if (p < toks.length) throw new Error(`Unexpected "${toks[p].v}" near the end of the query.`);

    return { select, distinct, from, fromAlias, joins, where, groupBy, having, orderBy, limit };

    /* ---- expressions ---- */
    function parseOr() {
      let left = parseAnd();
      while (atKw("OR")) { p++; left = { op: "OR", l: left, r: parseAnd() }; }
      return left;
    }
    function parseAnd() {
      let left = parseNot();
      while (atKw("AND")) { p++; left = { op: "AND", l: left, r: parseNot() }; }
      return left;
    }
    function parseNot() {
      // A bare NOT is a prefix, unless it starts "NOT IN" / "NOT LIKE"
      // (handled in parseCondition).
      if (atKw("NOT") && !(atKw("IN", 1) || atKw("LIKE", 1))) {
        p++;
        return { op: "NOT", e: parseNot() };
      }
      if (peek() && peek().t === "lp") {
        p++;
        const e = parseOr();
        expect("rp", "a closing parenthesis");
        return e;
      }
      return parseCondition();
    }
    function parseCondition() {
      const l = parseOperand();
      if (atKw("IS")) {
        p++;
        let neg = false;
        if (atKw("NOT")) { neg = true; p++; }
        eatKw("NULL");
        return { op: "ISNULL", e: l, neg };
      }
      let neg = false;
      if (atKw("NOT") && (atKw("IN", 1) || atKw("LIKE", 1))) { neg = true; p++; }
      if (atKw("IN")) {
        p++;
        expect("lp", "an opening parenthesis after IN");
        const list = [parseOperand()];
        while (peek() && peek().t === "comma") { p++; list.push(parseOperand()); }
        expect("rp", "a closing parenthesis after IN");
        return { op: "IN", l, list, neg };
      }
      if (atKw("LIKE")) {
        p++;
        const pat = expect("str", "a LIKE pattern in quotes").v;
        return { op: "LIKE", l, pat, neg };
      }
      if (atKw("BETWEEN")) {
        p++;
        const lo = parseOperand();
        eatKw("AND");
        const hi = parseOperand();
        return { op: "BETWEEN", l, lo, hi };
      }
      const tok = next();
      if (!tok || tok.t !== "op") throw new Error("Expected a comparison like =, > or < (or IN / LIKE / IS NULL / BETWEEN).");
      return { op: "CMP", cmp: tok.v, l, r: parseOperand() };
    }
    function parseOperand() {
      const tok = next();
      if (!tok) throw new Error("The condition ends too early.");
      if (tok.t === "num" || tok.t === "str") return { kind: "lit", v: tok.v };
      if (tok.t === "id") {
        if (peek() && peek().t === "lp") {
          next();
          const fn = tok.v.toUpperCase();
          if (!AGGS.has(fn)) throw new Error(`${tok.v}() is not a function I support here.`);
          let arg = "*";
          if (peek() && peek().t === "star") next();
          else if (peek() && peek().t === "id") arg = next().v;
          expect("rp", "a closing parenthesis");
          return { kind: "agg", fn, arg };
        }
        return { kind: "col", name: tok.v };
      }
      throw new Error("Expected a value or a column name in the condition.");
    }
  }

  /* ---- evaluation ---- */
  function likeRegex(pat) {
    let out = "^";
    for (const ch of pat) {
      if (ch === "%") out += "[\\s\\S]*";
      else if (ch === "_") out += "[\\s\\S]";
      else out += ch.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
    }
    return new RegExp(out + "$", "i");
  }

  function run(db, sql) {
    const ast = parse(sql);

    const table = (name) => {
      const t = db.find((t) => t.name.toLowerCase() === name.toLowerCase());
      if (!t) throw new Error(`There is no table called "${name}".`);
      return t;
    };

    const slots = [];
    const colIndex = new Map();
    const register = (names, cols) => cols.forEach((c) => {
      const idx = slots.push({ col: c }) - 1;
      for (const n of names) colIndex.set(`${n}.${c}`.toLowerCase(), idx);
      const plain = c.toLowerCase();
      if (!colIndex.has(plain)) colIndex.set(plain, idx);
    });
    const lookup = (name) => {
      const k = name.toLowerCase();
      if (colIndex.has(k)) return colIndex.get(k);
      throw new Error(`There is no column called "${name}".`);
    };

    const base = table(ast.from);
    register([base.name, ast.fromAlias].filter(Boolean), base.columns);
    let rows = base.rows.map((r) => r.slice());

    for (const j of ast.joins) {
      const jt = table(j.table);
      register([jt.name, j.alias].filter(Boolean), jt.columns);
      const joined = [];
      for (const cur of rows) {
        for (const jr of jt.rows) {
          const combined = cur.concat(jr);
          if (evalCond(j.on, combined, null)) joined.push(combined);
        }
      }
      rows = joined;
    }

    if (ast.where) rows = rows.filter((r) => evalCond(ast.where, r, null));

    /* ---- grouping ---- */
    let groups;
    if (ast.groupBy && ast.groupBy.length) {
      const idxs = ast.groupBy.map(lookup);
      const map = new Map();
      for (const r of rows) {
        const key = JSON.stringify(idxs.map((i) => r[i]));
        if (!map.has(key)) map.set(key, []);
        map.get(key).push(r);
      }
      groups = [...map.values()];
    } else {
      groups = [rows];
    }

    /* ---- HAVING (evaluated per group, with aggregates available) ---- */
    if (ast.having) groups = groups.filter((g) => evalCond(ast.having, null, g));

    // Function declarations (not consts) so they are hoisted above the WHERE /
    // JOIN evaluation that calls evalCond -> evalOperand -> aggValue.
    function aggValue(s, group) {
      if (s.fn === "COUNT" && s.arg === "*") return group.length;
      const idx = lookup(s.arg);
      const vals = group.map((r) => r[idx]).filter((v) => v !== null && v !== undefined);
      if (s.fn === "COUNT") return vals.length;
      if (!vals.length) return null;
      if (s.fn === "SUM") return vals.reduce((a, b) => a + b, 0);
      if (s.fn === "AVG") return vals.reduce((a, b) => a + b, 0) / vals.length;
      if (s.fn === "MIN") return Math.min(...vals);
      return Math.max(...vals);
    }
    function evalOperand(n, row, group) {
      if (n.kind === "lit") return n.v;
      if (n.kind === "agg") return aggValue(n, group || []);
      return row ? row[lookup(n.name)] : undefined;
    }

    const starOnly = ast.select.some((s) => s.kind === "star");
    if (starOnly && ast.select.length !== 1) throw new Error("Use * on its own, not mixed with column names.");
    const hasAgg = ast.select.some((s) => s.kind === "agg");
    const plainCols = ast.select.filter((s) => s.kind === "col" || s.kind === "star");
    if (hasAgg && plainCols.length && !ast.groupBy) {
      throw new Error("Mixing plain columns with aggregate functions needs GROUP BY.");
    }
    if (hasAgg && plainCols.length && ast.groupBy) {
      const grouped = new Set(ast.groupBy.map((n) => n.toLowerCase().split(".").pop()));
      for (const s of plainCols) {
        if (s.kind === "star" || !grouped.has(s.name.toLowerCase().split(".").pop())) {
          throw new Error(`Column ${s.name} must appear in GROUP BY or be used in an aggregate.`);
        }
      }
    }

    const outName = (s) => {
      if (s.alias) return s.alias;
      if (s.kind === "col") return s.name.split(".").pop();
      if (s.kind === "agg") return `${s.fn}(${s.arg})`;
      return "";
    };

    let outCols, outRows, srcRows;
    if (starOnly) {
      outCols = slots.map((s) => s.col);
      srcRows = rows;
      outRows = rows.map((r) => r.slice());
    } else if (hasAgg) {
      const idxs = ast.select.map((s) => (s.kind === "col" ? lookup(s.name) : -1));
      outCols = ast.select.map(outName);
      outRows = groups.map((g) => ast.select.map((s, i) =>
        s.kind === "agg" ? aggValue(s, g) : (g[0] ? g[0][idxs[i]] : null)));
      srcRows = groups.map((g) => g[0] || []);
    } else {
      const idxs = ast.select.map((s) => lookup(s.name));
      outCols = ast.select.map(outName);
      srcRows = rows;
      outRows = rows.map((r) => idxs.map((i) => r[i]));
    }

    if (ast.distinct) {
      const seen = new Set();
      const keptRows = [], keptSrc = [];
      outRows.forEach((r, i) => {
        const key = JSON.stringify(r);
        if (!seen.has(key)) { seen.add(key); keptRows.push(r); keptSrc.push(srcRows[i]); }
      });
      outRows = keptRows; srcRows = keptSrc;
    }

    /* ---- ORDER BY ---- */
    if (ast.orderBy) {
      const name = ast.orderBy.col.toLowerCase();
      const short = name.split(".").pop();
      let outIdx = outCols.findIndex((c) => c.toLowerCase() === name || c.toLowerCase() === short);
      let srcIdx = -1;
      try { srcIdx = lookup(ast.orderBy.col); } catch { /* not a source column */ }
      const desc = ast.orderBy.dir === "DESC";
      const key = (r, s) => {
        if (outIdx >= 0) return r[outIdx];
        if (srcIdx >= 0) return s ? s[srcIdx] : undefined;
        throw new Error(`Cannot ORDER BY "${ast.orderBy.col}" — it isn't in the result.`);
      };
      const pairs = outRows.map((r, i) => ({ r, s: srcRows[i] }));
      pairs.sort((a, b) => {
        const x = key(a.r, a.s), y = key(b.r, b.s);
        let c = 0;
        if (x === null || x === undefined) c = (y === null || y === undefined) ? 0 : -1;
        else if (y === null || y === undefined) c = 1;
        else c = x < y ? -1 : x > y ? 1 : 0;
        return desc ? -c : c;
      });
      outRows = pairs.map((p) => p.r);
    }

    if (ast.limit !== null) outRows = outRows.slice(0, ast.limit);
    return { columns: outCols, rows: outRows };

    function evalCond(n, row, group) {
      if (!n) return true;
      if (n.op === "AND") return evalCond(n.l, row, group) && evalCond(n.r, row, group);
      if (n.op === "OR") return evalCond(n.l, row, group) || evalCond(n.r, row, group);
      if (n.op === "NOT") return !evalCond(n.e, row, group);
      if (n.op === "ISNULL") {
        const v = evalOperand(n.e, row, group);
        const isNull = v === null || v === undefined;
        return n.neg ? !isNull : isNull;
      }
      const a = evalOperand(n.l, row, group);
      switch (n.op) {
        case "IN": {
          const hit = n.list.some((o) => evalOperand(o, row, group) === a);
          return n.neg ? !hit : hit;
        }
        case "LIKE": {
          const hit = typeof a === "string" && likeRegex(n.pat).test(a);
          return n.neg ? !hit : hit;
        }
        case "BETWEEN": {
          const lo = evalOperand(n.lo, row, group), hi = evalOperand(n.hi, row, group);
          return a >= lo && a <= hi;
        }
        case "CMP": {
          const b = evalOperand(n.r, row, group);
          switch (n.cmp) {
            case "=": return a === b;
            case "!=": return a !== b;
            case "<": return a < b;
            case ">": return a > b;
            case "<=": return a <= b;
            case ">=": return a >= b;
          }
          return false;
        }
      }
      return false;
    }
  }

  return { run, parse, tokenize };
})();

if (typeof module !== "undefined" && module.exports) module.exports = SQL;
if (typeof window !== "undefined") window.SQL = SQL;
