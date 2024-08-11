import string
from mutagen.easyid3 import EasyID3
import os

Surahnames = [
        "الفاتحة"
        ,"البقرة"
        ,"آل عمران"
        ,"النساء"
        ,"المائدة"
        ,"الأنعام"
        ,"الأعراف"
        ,"الأنفال"
        ,"التوبة"
        ,"يونس"
        ,"هود"
        ,"يوسف"
        ,"الرعد"
        ,"إبراهيم"
        ,"الحجر"
        ,"النحل"
        ,"الإسراء"
        ,"الكهف"
        ,"مريم"
        ,"طه"
        ,"الأنبياء"
        ,"الحج"
        ,"المؤمنون"
        ,"النور"
        ,"الفرقان"
        ,"الشعراء"
        ,"النمل"
        ,"القصص"
        ,"العنكبوت"
        ,"الروم"
        ,"لقمان"
        ,"السجدة"
        ,"الأحزاب"
        ,"سبأ"
        ,"فاطر"
        ,"يس"
        ,"الصافات"
        ,"ص"
        ,"الزمر"
        ,"غافر"
        ,"فصلت"
        ,"الشورى"
        ,"الزخرف"
        ,"الدخان"
        ,"الجاثية"
        ,"الأحقاف"
        ,"محمد"
        ,"الفتح"
        ,"الحجرات"
        ,"ق"
        ,"الذاريات"
        ,"الطور"
        ,"النجم"
        ,"القمر"
        ,"الرحمن"
        ,"الواقعة"
        ,"الحديد"
        ,"المجادلة"
        ,"الحشر"
        ,"الممتحنة"
        ,"الصف"
        ,"الجمعة"
        ,"المنافقون"
        ,"التغابن"
        ,"الطلاق"
        ,"التحريم"
        ,"الملك"
        ,"القلم"
        ,"الحاقة"
        ,"المعارج"
        ,"نوح"
        ,"الجن"
        ,"المزمل"
        ,"المدثر"
        ,"القيامة"
        ,"الإنسان"
        ,"المرسلات"
        ,"النبأ"
        ,"النازعات"
        ,"عبس"
        ,"التكوير"
        ,"الإنفطار"
        ,"المطففين"
        ,"الإنشقاق"
        ,"البروج"
        ,"الطارق"
        ,"الأعلى"
        ,"الغاشية"
        ,"الفجر"
        ,"البلد"
        ,"الشمس"
        ,"الليل"
        ,"الضحى"
        ,"الشرح"
        ,"التين"
        ,"العلق"
        ,"القدر"
        ,"البينة"
        ,"الزلزلة"
        ,"العاديات"
        ,"القارعة"
        ,"التكاثر"
        ,"العصر"
        ,"الهمزة"
        ,"الفيل"
        ,"قريش"
        ,"الماعون"
        ,"الكوثر"
        ,"الكافرون"
        ,"النصر"
        ,"المسد"
        ,"الإخلاص"
        ,"الفلق"
        ,"الناس"
]

def get_files_in_directory(directory):
    files = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            print(filename)
            for surahname in Surahnames:
                index = filename.find(surahname)
                
                if index != -1:
                    append_to_file(f'<Surah Idx="{index}" ContentRefrence="{filename}" Duration="25:30"/>')
                    
                index = -1
            
    return files

def append_to_file( data):
    try:
        with open("Surahnames.xml", 'a' ,encoding='utf-8') as file:
            file.write(data)
            file.write('\n')  # Optionally, add a newline after each entry
    except Exception as e:
        print("Error:", e)

directory_path = './'
all_files = get_files_in_directory(directory_path)
print("All files in directory:", all_files)