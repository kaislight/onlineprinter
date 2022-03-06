$(document).ready(function(){
    $('form input').change(function () {
      $('form p').text("已选择" + this.files.length + "个文件");
    });
  });