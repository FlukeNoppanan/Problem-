# 1. นาย ณพนันท์ ศรีเกื้อกลิ่น 6706022510204 , 2. นาย ศุภกร สิริเกื้อกูลชัย 6706022510174 , 3. นาย เจตริล เจริญทอง 6706022510425
Thailand = {'NORTH': ['CHIANG MAI', 'CHIANG RAI', 'LAMPANG', 'LAMPHUN', 'MAE HONG SON', 'NAN', 'PHAYAO', 'PHRAE', 'UTTARADIT'], 
            'NORTHEAST': ['AMNAT CHAROEN', 'BUENG KAN', 'BURI RAM', 'CHAIYAPHUM', 'KALASIN', 'KHON KAEN', 'LOEI', 'MAHA SARAKHAM', 'MUKDAHAN', 'NAKHON PHANOM', 'NAKHON RATCHASIMA', 'NONG BUA LAM PHU', 'NONG KHAI', 'ROI ET', 'SAKON NAKHON', 'SI SA KET', 'SURIN', 'UBON RATCHATHANI', 'UDON THANI', 'YASOTHON'], 
            'CENTRAL': ['ANG THONG', 'BANGKOK', 'CHAI NAT', 'KAMPHAENG PHET', 'LOP BURI', 'NAKHON NAYOK', 'NAKHON PATHOM', 'NAKHON SAWAN', 'NONTHABURI', 'PATHUM THANI', 'PHRA NAKHON SI AYUTTHAYA', 'PHICHIT', 'PHITSANULOK', 'SAMUT PRAKAN', 'SAMUT SAKHON', 'SAMUT SONGKHRAM', 'SARABURI', 'SING BURI', 'SUPHAN BURI', 'UTHAI THANI'], 
            'SOUTH': ['CHUMPHON', 'KRABI', 'NAKHON SI THAMMARAT', 'NARATHIWAT', 'PATTANI', 'PHANG NGA', 'PHATTHALUNG', 'PHUKET', 'RANONG', 'SATUN', 'SONGKHLA', 'SURAT THANI', 'TRANG', 'YALA'], 
            'EAST': ['CHACHOENGSAO', 'CHANTHABURI', 'CHON BURI', 'PRACHIN BURI', 'RAYONG', 'SA KAEO', 'TRAT'], 
            'WEST': ['KANCHANABURI', 'PHETCHABURI', 'PRACHUAP KHIRI KHAN', 'RATCHABURI', 'TAK']}

def InsertData(dict):
    key = input("Please enter the name of the region.: ")
    value = input("Please enter the name of the province.: ")
    if key == '':
        return print("Please enter the name of the region.")
    if key.upper() in dict:
        if value == '':
            return print("Please enter the name of the province.")
        if value.upper() in dict[key.upper()]:
            return print("The information is already in the system.")
        dict[key.upper()].append(value.upper())
    else:
        if value == '':
            dict[key.upper()] = []
        else:
            dict[key.upper()] = [value.upper()]
    return print("Information added successfully.")

def UpdateData(input_value,dict):
    for region, province in dict.items():
        if input_value.upper() in province:
            print(f"province {input_value} in {region}")
            new_province = input("Please enter the new province name: ")
            if new_province == '':
                return print("Please enter the new province name.")
            if new_province.upper() in province:
                return print("The information is already in the system.")
            province[province.index(input_value.upper())] = new_province.upper()
            return print("Information updated successfully.")
    return print("No information found.")


def SearchData(s,dict):
    for key, value in dict.items():
        for i in value:
            if i == s.upper():
                return print(f"province {s.upper()} in {key}")
    return print("No information found.")

def DeleteData(input_value,dict,is_region=False):
    if is_region:
        if input_value.upper() in dict:
            del dict[input_value.upper()]
            return print("Information deleted successfully")
        print("No information found.")
    else:
        for key, value in dict.items():
            if input_value.upper() in value:
                value.remove(input_value.upper())
                return print("Information deleted successfully")
        print("No information found.")

def ViewAllData(data_dict):
    for key, values in data_dict.items():
        print(f"{key}:")
        for i, value in enumerate(values, 1):
            print(f"  {value}", end=" | " if i % 4 != 0 else " |\n")  
        print("\n") 

def main():
    while True:
        print("------------------------------------------------")
        print("Welcome to the program")
        print("select the menu")
        print("1. InsertData")
        print("2. UpdateData")
        print("3. SearchData")
        print("4. DeleteData")
        print("5. ViewAllData")
        print("6. Exit the program")
        try:
            choice = int(input("Please select menu: "))
        except ValueError:
            print("Please select again , only number 1-6 are available")
            continue
        print("------------------------------------------------")
        if choice == 1:
            InsertData(Thailand)
        elif choice == 2:
            s = input("Please enter the name of the province you want to edit: ")
            UpdateData(s, Thailand)
        elif choice == 3:
            s = input("Please enter the name of the province you want to search: ")
            SearchData(s, Thailand)
        elif choice == 4:
            print("DeleteData")
            print("1. region")
            print("2. province")
            choice1 = int(input("Please select menu: "))
            if choice1 == 1:
                s = input("Please enter the name of the region you want to delete: ")
                DeleteData(s, Thailand, True)
            elif choice1 == 2:
                s = input("Please enter the name of the province you want to delete: ")
                DeleteData(s, Thailand, False)
            else:
                print("Please select again.")
        elif choice == 5:
            ViewAllData(Thailand)
        elif choice == 6:
            print("Exit the program")
            print("Thank you for using the program")
            print("------------------------------------------------")
            break
        else:
            print("Please select again , only number 1-6")

main()