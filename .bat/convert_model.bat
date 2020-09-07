@echo OFF
set caffe_dir=H:\\software\\caffe_1\\caffe\\build\\tools

set caffemodel=ti_models\\global2.caffemodel
set save_root=ti_models\\global2
if not exist %save_root%	mkdir %save_root%
set convert_model_name=global2_convert

echo "====================convert configs====================="
echo %caffemodel%
echo %save_root%
echo %convert_model_name%

%caffe_dir%\\Release\\convert_model %caffemodel% %save_root% %convert_model_name%

echo "====================convert Done====================="
START /WAIT
