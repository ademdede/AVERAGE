
# Yazilimi komut arayuzu uzerinden girilen ders notlarini hafizada
# tutup girilen tum notlarin agirlikli ortalamasini
# hesaplayan bir yazilim yaziniz

# format: "komut      ogrenci_no       ogrenci_adi              not_carpani_5yildiza_kadar         alinan_not_1_100"

# ornek Input: "add  123   Ali_Yigit_Can  fen   ***   90"
# ornek Print:
# [ {student_id: 123, name: "Ali Yigit Can", ortalama:80, notlar:
#     [{katsayi: 1, not:50, created_at: "12/24/2018, 04:59:31"},
#      {katsayi:3, not:90, created_at: "12/24/2018, 04:59:31"}] },
#  {student_id: 124, name: "Musa Can",  ortalama:75, notlar:
#      [{katsayi: 3, not:60, created_at: "12/24/2018, 05:59:31"},
#       {katsayi:3, not:90, created_at: "12/24/2018, 05:59:31"}] } ]
#  input example : add student_no student_name stars grade
# def index_finder():
#     index = (i for i, sname in data_list)
#     if sname == data_list[1]:
#         return index
#     print(index)
# add  123   Mustafa  fen   *****  100
# add  555   Murat  fen   *****  10

from tools import crud_student, crud_grades, print_data


student_list = []

while True:
    try:
        teacher_input = input("Please enter your command (q for quit):")

        if teacher_input == "q":
            print("Application exited.")
            break
        splitted_data = teacher_input.split()
        if splitted_data[0] == "add":
            crud_student(splitted_data)
            crud_grades(splitted_data)

        elif splitted_data[0] == "update":
            crud_grades(splitted_data)

        elif splitted_data[0] == "print":
            print_data(splitted_data[1])
        else:
            print("Wrong input")

    except:

        print("Something went wrong. Try again")

