user_id=$(id -u)
device_name="$(ls -A /run/user/${user_id}/gvfs)"

if [ -z "$device_name" ]; then
    echo "Device not found"
else
    telegram_files=5
    whatsapp_files=10
    vk_files=10

    echo "Device found: ${device_name}"

    user_name=$(whoami)

    save_path="/home/${user_name}/Desktop/${device_name}"
    
    #if directory does not exist
    if [ ! -d "${save_path}" ]; then
        mkdir ${save_path}
    fi

    echo "Directory created: ${save_path}"

    device_path="/run/user/1000/gvfs/${device_name}"

    echo "Device Path: ${device_path}"
    cd ${device_path}

    telegram_path=$(find . -maxdepth 3 -type d -name "Telegram" | tail -n 1)
    whatsapp_path=$(find . -maxdepth 3 -type d -name "WhatsApp" | tail -n 1)
    vk_path=$(find . -maxdepth 3 -type d -name "VK" | tail -n 1)

    telegram_save_path=""
    whatsapp_save_path=""
    vk_save_path=""

    if ! [ -z "$telegram_path" ]; then
        cd ${device_path}
        echo "Telegram path: ${telegram_path}"
        
        telegram_save_path="${save_path}/Telegram"
        
        #if directory does not exist
        if [ ! -d "${telegram_save_path}" ]; then
            mkdir ${telegram_save_path}
        fi

        cd "${telegram_path}"

        #find -P . -type f -name "*.jpg" -printf "%T@ %Tc %p\n" | sort -r | cut -d " " -f8 | head -n ${telegram_files} | while read file_name
        find -P . -type f -name "*.jpg" | head -n ${telegram_files} | while read file_name
        do
            echo "Copying: ${file_name}"
            cp "$file_name" "$telegram_save_path"
        done
    else
        echo "Telegram path not found"
    fi
    
    exit

    if ! [ -z "$whatsapp_path" ]; then
        cd ${device_path}
        echo "WhatsApp path: ${whatsapp_path}"
        
        whatsapp_save_path="${save_path}/WhatsApp"
        
        #if directory does not exist
        if [ ! -d "${whatsapp_save_path}" ]; then
            mkdir ${whatsapp_save_path}
        fi

        cd "${whatsapp_path}"

        #find -P . -type f -name "*.jpg" -printf "%T@ %Tc %p\n" | sort -r | cut -d " " -f8 | head -n ${whatsapp_files} | while read file_name
        find -P . -type f -name "*.jpg" | head -n ${whatsapp_files} | while read file_name
        do
            echo "Copying: ${file_name}"
            cp "$file_name" "$whatsapp_save_path"
        done
    else
        echo "WhatsApp path not found"
    fi

    if ! [ -z "$vk_path" ]; then
        cd ${device_path}
        echo "VK path: ${vk_path}"
        
        vk_save_path="${save_path}/VK"
        
        #if directory does not exist
        if [ ! -d "${vk_save_path}" ]; then
            mkdir ${vk_save_path}
        fi

        cd "${vk_path}"

        #find -P . -type f -name "*.jpg" -printf "%T@ %Tc %p\n" | sort -r | cut -d " " -f8 | head -n ${vk_files} | while read file_name
        find -P . -type f -name "*.jpg" | head -n ${vk_files} | while read file_name
        do
            echo "Copying: ${file_name}"
            cp "$file_name" "$vk_save_path"
        done
    else
        echo "VK path not found"
    fi
fi
