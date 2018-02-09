%define debug_package %{nil}

Summary:	File and archive manager
Name:		peazip
Version:	6.5.0
Release:	1
License:	LGPLv3+
Group:		File tools
Url:		http://www.peazip.org
Source0:	https://sourceforge.net/projects/peazip/files/%{version}/%{name}-%{version}.src.zip
# configure to run in users home appdata
Source1:	altconf.txt
BuildRequires:	dos2unix >= 7.3
BuildRequires:	lazarus >= 1.2.0
BuildRequires:	qt4pas-devel
BuildRequires:	qt4-devel
# BuildRequires:	qtwebkit-devel
BuildRequires:	icoutils
Requires:	p7zip
Requires:	upx >= 3.09

%description
PeaZip is a free cross-platform file archiver that provides an unified
portable GUI for many Open Source technologies like 7-Zip, FreeArc, PAQ,
UPX...

#---------------------------------------------------------------------

%prep
%setup -qn %{name}-%{version}.src
chmod +w res/lang
dos2unix readme*

%build
lazbuild --lazarusdir=%{_libdir}/lazarus \
%ifarch x86_64
	--cpu=x86_64 \
%endif
	--widgetset=qt \
	-B project_peach.lpi project_pea.lpi project_gwrap.lpi

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/%{name}
rm -rf res/icons
cp -r res %{buildroot}%{_datadir}/%{name}
cp %{SOURCE1} %{buildroot}%{_datadir}/%{name}/res

#install helper apps
mkdir -p %{buildroot}%{_datadir}/%{name}/res/{7z,upx}
ln -s %{_bindir}/7z  %{buildroot}%{_datadir}/%{name}/res/7z
ln -s %{_bindir}/upx  %{buildroot}%{_datadir}/%{name}/res/upx

install pea %{buildroot}%{_datadir}/%{name}/res
ln -s %{_datadir}/%{name}/res/pea %{buildroot}%{_bindir}/pea
install %{name} %{buildroot}%{_datadir}/%{name}
ln -s %{_datadir}/%{name}/%{name} %{buildroot}%{_bindir}/%{name}
install pealauncher %{buildroot}%{_datadir}/%{name}/res
ln -s %{_datadir}/%{name}/res/pealauncher %{buildroot}%{_bindir}/pealauncher

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=PeaZip
GenericName=Archiving Tool
GenericName[af]=Argiveer Program
GenericName[ar]=أداة أرشفة
GenericName[ast]=Ferramienta p'archivar
GenericName[bg]=Работа с архиви
GenericName[br]=Ostilh merañ an Dielloù
GenericName[bs]=Alatka za arhiviranje
GenericName[ca]=Eina d'arxivament
GenericName[ca@valencia]=Eina d'arxivament
GenericName[cs]=Archivační nástroj
GenericName[cy]=Erfyn Archifo
GenericName[da]=Arkiveringsværktøj
GenericName[de]=Archivprogramm
GenericName[el]=Εργαλείο αρχειοθέτησης
GenericName[en_GB]=Archiving Tool
GenericName[eo]=Arkivilo
GenericName[es]=Archivador
GenericName[et]=Arhiivide haldamise rakendus
GenericName[eu]=Artxibatzeko Tresna
GenericName[fa]=ابزار بایگانی
GenericName[fi]=Pakkausohjelma
GenericName[fr]=Outil d'archivage
GenericName[ga]=Uirlis Chartlannaithe
GenericName[gl]=Utilidade de arquivo
GenericName[he]=כלי לניהול ארכיונים
GenericName[hne]=अभिलेखन औजार
GenericName[hr]=Alat za arhiviranje
GenericName[hu]=Fájltömörítő
GenericName[ia]=Instrumento per archivar
GenericName[id]=Perkakas Pengarsip
GenericName[is]=Vinna með safnskrár
GenericName[it]=Strumento di archiviazione
GenericName[ja]=アーカイブツール
GenericName[kk]=Архивтеу құралы
GenericName[km]=ឧបករណ៍ប័ណ្ណសារ
GenericName[ko]=압축 도구
GenericName[lt]=Archyvavimo priemonė
GenericName[lv]=Arhivēšanas rīks
GenericName[mk]=Алатка за архивирање
GenericName[ms]=Alatan Pengarkiban
GenericName[nb]=Arkiveringsverktøy
GenericName[nds]=Archievwarktüüch
GenericName[ne]=सङ्ग्रहण उपकरण
GenericName[nl]=Archiefgereedschap
GenericName[nn]=Arkiveringsverktøy
GenericName[pa]=ਅਕਾਇਵਿੰਗ ਟੂਲ
GenericName[pl]=Narzędzie do archiwizacji
GenericName[pt]=Ferramenta de Armazenamento
GenericName[pt_BR]=Ferramenta de Arquivamento
GenericName[ro]=Utilitar de arhivare
GenericName[ru]=Архиватор
GenericName[sk]=Archivačný nástroj
GenericName[sl]=Orodje za ravnanje z arhivi
GenericName[sq]=Mjeti Arkivues
GenericName[sr]=Алатка за архивирање
GenericName[sr@ijekavian]=Алатка за архивирање
GenericName[sr@ijekavianlatin]=Alatka za arhiviranje
GenericName[sr@latin]=Alatka za arhiviranje
GenericName[sv]=Arkiveringsverktyg
GenericName[ta]=காப்பக கருவி
GenericName[tg]=Асбобҳои Бойгонӣ
GenericName[th]=เครื่องมือจัดการแฟ้มจัดเก็บ
GenericName[tr]=Arşivleme Aracı
GenericName[ug]=ئارخىپ قورالى
GenericName[uk]=Засіб роботи з архівами
GenericName[uz]=Arxivlash vositasi
GenericName[uz@cyrillic]=Архивлаш воситаси
GenericName[vi]=Công Cụ Nén
GenericName[wa]=Usteye d' årtchivaedje
GenericName[xh]=Isixhobo Sokuphatha i Archive
GenericName[x-test]=xxArchiving Toolxx
GenericName[zh_CN]=压缩归档工具
GenericName[zh_TW]=壓縮工具
Comment=Create and modify an archive
Comment[af]=Skep en wysig 'n argief
Comment[an]=Creye y modifique un archivador
Comment[ar]=أنشئ و عدّل أرشيفا
Comment[as]=আৰ্কাইভ সৃষ্টি ও পৰিবৰ্তন কৰক
Comment[ast]=Crea y modifica un archivador
Comment[az]=Arxiv yaradın və açın
Comment[be]=Праца з архівамі
Comment[be@latin]=Stvaraj i madyfikuj archivy
Comment[bg]=Създаване и промяна на архив
Comment[bn]=নতুন আর্কাইভ তৈরি ও পরিবর্ধন করা হবে
Comment[bn_IN]=আর্কাইভ নির্মাণ ও পরিবর্তন করুন
Comment[br]=Krouiñ ha daskemmañ un diell
Comment[bs]=Napravi i promijeni arhiv
Comment[ca]=Crea i modifica un arxiu
Comment[ca@valencia]=Crea i modifica un arxiu
Comment[cs]=Vytvářet a upravovat archivy
Comment[csb]=Ùsôdzanié ë zmianë archiwów
Comment[cy]=Creu a newid archif
Comment[da]=Opret og ændr et arkiv
Comment[de]=Archive anlegen und verändern
Comment[dz]=ཡིག་མཛོད་གསར་བསྐྲུན་འབད་ནི་དང་ ལེགས་བཅོས་འབད་ནི།
Comment[el]=Δημιουργία και τροποποίηση ενός συμπιεσμένου αρχείου
Comment[en@shaw]=𐑒𐑮𐑦𐑱𐑑 𐑯 𐑥𐑪𐑛𐑦𐑓𐑲 𐑩𐑯 𐑸𐑒𐑲𐑝
Comment[en_CA]=Create and modify an archive
Comment[en_GB]=Create and modify an archive
Comment[eo]=Krei kaj modifi arkivon
Comment[es]=Cree y modifique un archivador
Comment[et]=Arhiivi loomine ja muutmine
Comment[eu]=Sortu eta aldatu artxibo bat
Comment[fa]=ایجاد و تغییر آرشیو
Comment[fi]=Luo arkisto tai muokkaa arkistoa
Comment[fr]=Créer et modifier des archives
Comment[fur]=Cree e modifiche un archivi
Comment[fy]=Foarmje in triemûnthâld
Comment[ga]=Cruthaigh agus athraigh cartlann
Comment[gl]=Crear e modificar un arquivo
Comment[gu]=પેટી બનાવો અને સુધારો
Comment[he]=יצירה ועדכון של ארכיונים
Comment[hi]=अभिलेख बनाएँ तथा परिवर्धित करें
Comment[hr]=Stvori i izmijeni arhivu
Comment[hu]=Archívum létrehozása és módosítása
Comment[hy]=Կերտել և մոդիֆիկացնել արխիվը
Comment[id]=Membuat dan memodifikasi arsip
Comment[it]=Crea e modifica un archivio
Comment[ja]=アーカイブを作成したり修正します
Comment[ka]=არქივის შექმნა და რედაქტირება
Comment[kk]=Архивті жасау және түзету
Comment[km]=បង្កើត និងកែប្រែប័ណ្ណសារ
Comment[kn]=ಒಂದು ಆರ್ಕೈವನ್ನು ನಿರ್ಮಿಸು ಹಾಗು ಮಾರ್ಪಡಿಸು
Comment[ko]=압축 파일을 만들고 수정합니다
Comment[ku]=Arşîvekê çêbike an jî biguherîne
Comment[lt]=Kurti ir modifikuoti archyvą
Comment[lv]=Izveidot arhīvus un mainīt to saturu
Comment[mai]=अभिलेख बनाबू आओर परिवर्धित करू
Comment[mg]=Mamorona sy manova arsiva
Comment[mk]=Креирај и измени архива
Comment[ml]=ഒരു പുതിയ ശേഖരം നിര്മ്മിക്കുകയോ മാറ്റം വരുത്തുകയോ ചെയ്യുക
Comment[mn]=Архив үүсгэх ба өөрчилөх
Comment[mr]=आर्काइव्ह निर्माण व संपादीत करा
Comment[ms]=Cipta dan ubahsuai arkib
Comment[my]=ဖိုင်ထုပ်ကိုဖန်တီးပြီးပြုပြင်
Comment[nb]=Opprett og endre arkiv
Comment[ne]=एउटा सङ्ग्रह सिर्जना गर्नुहोस् र परिमार्जन गर्नुहोस्
Comment[nl]=Archieven maken en wijzigen
Comment[nn]=Lag og endra arkiv
Comment[oc]=Crear e modificar un archiu
Comment[or]=ଗୋଟିଏ ଅଭିଲେଖକୁ ସ୍ରୁଷ୍ଟି ଏବଂ ରୂପାନ୍ତରିତ କରନ୍ତୁ
Comment[pa]=ਇੱਕ ਅਕਾਇਵ ਬਣਾਓ ਅਤੇ ਸੋਧੋ
Comment[pl]=Tworzenie i modyfikowanie archiwów
Comment[ps]=ارشيو جوړول او بدلول
Comment[pt]=Criar e alterar um arquivo
Comment[pt_BR]=Crie e modifique um pacote
Comment[ro]=Creează și modifică o arhivă
Comment[ru]=Создать или изменить архив
Comment[si]=සංරක්ෂණයක් නිර්මාණය කරන්න සහ වෙනස් කරන්න
Comment[sk]=Vytváranie a úprava archívov
Comment[sl]=Ustvari in spremeni arhiv
Comment[sq]=Krijo dhe ndrysho një arkiv
Comment[sr]=Направите нове и распакујте постојеће архиве
Comment[sr@ije]=Направите и измјените архиву
Comment[sr@latin]=Napravite nove i raspakujte postojeće arhive
Comment[sv]=Skapa och ändra ett arkiv
Comment[ta]=காப்பு உருவாக்குதல் அல்லது திருத்துதல்
Comment[te]=ఒక సంగ్రహమును సృష్టించు మరియు సవరించు
Comment[th]=สร้างและแก้ไขแฟ้มจัดเก็บ
Comment[tk]=Bir arşiwi bejerip üýtget
Comment[tr]=Bir arşiv yarat ve değiştir
Comment[ug]=ئارخىپ قۇرۇپ ئۆزگەرت
Comment[uk]=Програма створення та зміни архівів
Comment[ur]=محفوظہ بنائیں اور تبدیل کریں
Comment[ur_PK]=محفوظہ بنائیں اور تبدیل کریں
Comment[vi]=Tạo và sửa đổi kho
Comment[xh]=Yakha uze ulungise uvimba
Comment[zh_CN]=创建并修改归档文件
Comment[zh_HK]=建立及更改壓縮檔
Comment[zh_TW]=建立及更改壓縮檔
Comment[zu]=Dala futhi ulungise ingobo yomlando
MimeType=application/x-gzip;application/x-lha;application/x-tar;application/x-tgz;application/x-tbz;application/x-tbz2;application/x-zip;application/zip;application/x-bzip;application/x-rar;application/x-tarz;application/x-archive;application/x-bzip2;application/x-jar;application/x-deb;application/x-ace;application/x-7z;application/x-arc;application/x-arj;application/x-compress;application/x-cpio;
Exec=%{name}
Icon=%{name}
Type=Application
Terminal=false
Categories=KDE;GTK;Utility;Archiving;
EOF

mkdir -p %{buildroot}%{_iconsdir}/hicolor/256x256/apps
icotool -x -i 1 -o %{buildroot}%{_iconsdir}/hicolor/256x256/apps/%{name}.png %{name}.ico
rm -rf %{buildroot}%{_datadir}/%{name}/res/icons

%files
%doc readme copying.txt
%{_bindir}/*
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/applications/*.desktop
%{_datadir}/%{name}
