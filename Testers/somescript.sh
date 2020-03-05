RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'
tests_number=10
passed=1
for (( c=1; c<=${tests_number}; c++ ))
do  
	if [ $c -eq ${tests_number} ]; then
		echo "Test [${c}/${tests_number}]"
	else
		echo -en "Test [${c}/${tests_number}]" "\r"
	fi
	python3 gen.py > temp_test_file
	./my.out < temp_test_file > temp_my_res_file
	./his.out < temp_test_file > temp_his_res_file
	cmp temp_my_res_file temp_his_res_file > temp_logs
	if [ $? -eq 1 ];
	then
		echo ""
		cat temp_logs
		passed=0
		break
	fi 
	> temp_test_file
done
if [ ${passed} -eq 1 ]; then
	echo -e "${GREEN}PASSED${NC}"
	rm temp_my_res_file temp_his_res_file temp_test_file temp_logs
else
	echo -e "${RED}NOT PASSED${NC}"
fi
#rm temp_test_file temp_my_res_file temp_his_res_file
