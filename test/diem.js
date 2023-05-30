function tinhDiem() {
   
    // Lấy thông tin từ các ô nhập liệu
    var mssv = document.getElementById("mssv").value;
    var ten = document.getElementById("ten").value;
    var toan = parseFloat(document.getElementById("toan").value);
    var van = parseFloat(document.getElementById("van").value);
    var anh = parseFloat(document.getElementById("anh").value);
  
    // Tính điểm trung bình
    var diemTB = (toan + van + anh) / 3;
  
    // Hiển thị kết quả
    document.getElementById("diemTB").innerHTML = "MSSV: " + mssv + "<br>" +
      "Tên: " + ten + "<br>" +
      "Điểm trung bình: " + diemTB.toFixed(2);
  
    // Tạo nội dung file txt
    var noiDung = "MSSV: " + mssv + "\n" +
      "Tên: " + ten + "\n" +
      "Điểm trung bình: " + diemTB.toFixed(2);
  
    // Tạo đối tượng Blob
    var blob = new Blob([noiDung], { type: "text/plain;charset=utf-8" });

    // Tạo đường dẫn tải xuống file
    // var link = document.createElement("a");
    // link.download = "ket_qua.txt";
    // link.href = window.URL.createObjectURL(blob);
    // link.onclick = function() {
    //   // Xóa đối tượng Blob khi người dùng đã tải xuống file
    //   window.URL.revokeObjectURL(blob);
    //   link.remove();
    // };
  
    // Thêm đường dẫn vào trang web và kích hoạt sự kiện click
    document.body.appendChild(link);
    link.click();
    
}