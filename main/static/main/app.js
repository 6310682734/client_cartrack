Dropzone.autoDiscover = false;

var myDropzone = new Dropzone(element, {                      
  autoProcessQueue: false,
  paramName: 'file',
  clickable: true,
  maxFiles: 5,
  maxFilesize: 10,
});

$('#button-upload').click(function(){           
  myDropzone.processQueue();
});