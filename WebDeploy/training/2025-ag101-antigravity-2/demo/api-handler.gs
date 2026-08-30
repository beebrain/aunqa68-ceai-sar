function doPost(e) {
  try {
    var lock = LockService.getScriptLock();
    lock.waitLock(30000); // wait 30 seconds for lock
    
    var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
    
    // If sheet is empty, write headers first
    if (sheet.getLastRow() === 0) {
      sheet.appendRow(["Timestamp", "ชื่อ-สกุล", "อีเมล", "เบอร์โทร", "อาชีพ", "หัวข้อที่สนใจ"]);
    }
    
    var rawData = e.postData.contents;
    var data = JSON.parse(rawData);
    
    var rowData = [
      new Date(),
      data.name || "",
      data.email || "",
      data.phone || "",
      data.occupation || "",
      data.course || ""
    ];
    
    sheet.appendRow(rowData);
    
    return ContentService.createTextOutput(JSON.stringify({
      status: "success",
      message: "Data synchronized successfully"
    }))
    .setMimeType(ContentService.MimeType.JSON)
    .setHeader("Access-Control-Allow-Origin", "*")
    .setHeader("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
    .setHeader("Access-Control-Allow-Headers", "Content-Type");
    
  } catch (error) {
    return ContentService.createTextOutput(JSON.stringify({
      status: "error",
      message: error.toString()
    }))
    .setMimeType(ContentService.MimeType.JSON)
    .setHeader("Access-Control-Allow-Origin", "*")
    .setHeader("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
    .setHeader("Access-Control-Allow-Headers", "Content-Type");
  } finally {
    if (lock) {
      lock.releaseLock();
    }
  }
}

function doOptions(e) {
  return ContentService.createTextOutput("")
    .setMimeType(ContentService.MimeType.TEXT)
    .setHeader("Access-Control-Allow-Origin", "*")
    .setHeader("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
    .setHeader("Access-Control-Allow-Headers", "Content-Type");
}
