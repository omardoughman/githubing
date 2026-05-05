import initSqlJs from "sql.js";

let db;

export async function initDB(fileBuffer) {
  const SQL = await initSqlJs({
    locateFile: file => `https://sql.js.org/dist/${file}`
  });

  db = new SQL.Database(new Uint8Array(fileBuffer));
}

export function runQuery(query) {
  const result = db.exec(query);
  return result;
}

export function exportDB() {
  const data = db.export();
  return new Blob([data], { type: "application/octet-stream" });
}
