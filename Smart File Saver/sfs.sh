user_id=$(id -u)
res="$(ls -A /run/user/${user_id}/gvfs)"
if [ -z "$res" ]; then
	echo "Device not found"
else
	telegram_files=5
	whatsapp_files=10
	vk_files=10

	echo "Device found: ${res}"

	save_path="/home/zero/desktop/${res}"
	mkdir ${save_path}
	echo "Directory created: ${save_path}"

	device_path="/run/user/1000/gvfs/${res}"

	cd ${device_path}

	telegram_path=$(find . -maxdepth 3 -type d -name "Telegram")
	whatsapp_path=$(find . -maxdepth 3 -type d -name "WhatsApp")
	vk_path=$(find . -maxdepth 3 -type d -name "VK")

	telegram_save_path=""
	whatsapp_save_path=""
	vk_save_path=""

	if ! [ -z "$telegram_path" ]; then
		cd ${device_path}
		echo "Telegram path: ${telegram_path}"
		
		telegram_save_path="${save_path}/Telegram"
		mkdir $telegram_save_path
		
		cd "${telegram_path}"

		find . -type f -name "*.jpg" | head -n ${telegram_files} | while read file_name
		do
			echo $file_name
			cp "$file_name" "$telegram_save_path"
		done
	else
		echo "Telegram path not found"
	fi
	
	if ! [ -z "$whatsapp_path" ]; then
		cd ${device_path}
		echo "WhatsApp path: ${whatsapp_path}"
		
		whatsapp_save_path="${save_path}/WhatsApp"
		mkdir $whatsapp_save_path
		
		cd "${whatsapp_path}"

		find . -type f -name "*.jpg" | head -n ${whatsapp_files} | while read file_name
		do
			echo $file_name
			cp "$file_name" "$whatsapp_save_path"
		done
	else
		echo "WhatsApp path not found"
	fi

	if ! [ -z "$vk_path" ]; then
		cd ${device_path}
		echo "VK path: ${vk_path}"
		
		vk_save_path="${save_path}/VK"
		mkdir $vk_save_path
		
		cd "${vk_path}"

		find . -type f -name "*.jpg" | head -n ${vk_files} | while read file_name
		do
			echo $file_name
			cp "$file_name" "$vk_save_path"
		done
	else
		echo "VK path not found"
	fi
fi
