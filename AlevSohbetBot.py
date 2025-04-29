# bu kodlama ramazan Öztürk tarafından yapılmıştır amaç bir botu klonlamakti insta: @ramowlf

from pyrogram import *
from pyrogram.types import *
from pyrogram.enums import *
import random, asyncio, threading, yt_dlp, youtube_dl, json, os, requests
from gtts import gTTS
import gtts
from random import choice
bot = Client("ramazan_buba", api_id=27833866, api_hash="3648a12e9a8df3f448d4aeaac2ab91ab", bot_token="token gir")
bot.start()
bot.set_parse_mode(ParseMode.MARKDOWN)

tagging = {}
tag_users = {}
tag_text = {}

cokseksiyim=[
	"Seçtiğiniz bir sosyal medya hesabınızdan çok çirkin bir fotoğrafınızı paylaşın.","Mesaj yazma bölümünüzü telefonunuzdan açın gözlerinizi kapatın ve rasgele bir kişiye körü körüne bir metin gönderin.",
	"Önümüzdeki 5 dakika boyunca söylediğin her şeyden sonra “mee” diyeceksin",
	"Önümüzdeki 5 dakika içinde birinin hayvanı olun.","İnstagramını oyunculardan birine ver. 5 dk boyunca her yere bakmak serbest.",
	"Oyundan bir kişiye serenat yap (kız ise erkeğe, erkek ise kıza)","Sonraki 3 tur boyunca şiveyle konuş.",
	"3 dakika boyunca bebek taklidi yap!","Telefonunda ki en sevmediğin fotoğrafını at","En beğendiğin fotoğrafını at",
	"Whatsapp’da 2 konuşmanı at","Özel mesajlarını ssi al ve gruba at","Whatsapp’da son konuşmanı at",
	"Bir deftere 20 kez ben çatlağım yaz ve resmini at","Telegramda son konuşmanı ss at.","Biyografine +18 bir cümle yaz; 3 Saat duracak.!",
	"Galerinin bir kısmını ss alıp at","Galerindeki 16. Fotoğrafı at.","Instagram yada telegramdan tanımadığın birine komik olmayan bir fıkra anlat.",
	"Ninni Söyleyerek Ses At","Bugununle ilgili kısa bir hikaye uydur.","Grupta ki en çok hoşuna giden karşı cinse seni seviyorum diye mesaj at.",
	"Galerindeki 16. Fotoğrafı at.","Galerindeki 30. Fotoğrafı at.","Whatsapp’da konuşduğun kişilerin ss ini at",
	"Grubun üye listesine gir ve 7. kişiye anlık at. (Grup daha az kişiyse ya da aktif sayısı azsa üstten saymaya devam et)",
	"En son konuştuğun kişiye \"Hayırlı Cumalar\" diye mesaj at.(platform farketmez)",
	"Şuan ki halini fotoğraf çekip  atar mısın?","Grupta üyeler kısmına gir 11. kişiye \"Analar neler doğuruyor bee\" diye ses at ve cevabını grupla paylaş.",
	"Profil fotoğrafına nefret ettiğin bir ünlünün resmini koy.","Kafanda yumurta kır ve fotosunu at",
	"Gruptan sevdiğin bir kişinin fotoğrafını profil resmi yap","Balkona veya pencereye cık dısardakılerın duyacagı sekılde sarkı soyle videoya al gruba at.",
	"İtiraf et: üye çalmak için kaç hesabın var?","Gruptaki 5 abazaya seni seviyorum de","İki dakika tavuk gibi davran.","Seçtiğiniz bir hayvanı taklit edin.",
	"Seçtiğin bir nesneyi yalayın ve gruba fotosunu atın.","Gruba gerçekten utanç verici bir fotoğrafını göster.",
	"Çirkin bir selfie çek ve sosyal medya uygulamalarından birinde yayınla 1.5 saat kalacak.","Bir kaşık un ye ve video ya al gruba at",
	"Hiç tanımadığın birine Kurban Bayramınızı kutlarım deyin","Sevdiğin bir kişiye \"`ben seni neden sevdim niçin sevdim niye sevdim bunların bi izahı yok gördün işte sevdim. Yaw sahi ben seni nidennn sevdim `\" de. Cevap geldiğinde grupla paylaş biz de gülelim",
	"Telegram'daki en kalabalık grubu aç ve \"`Benim adım turşu bidonu!`\" diyerek ses kaydedip en kalabalık gruba gönder.","Hemcinsin olan yakın bir arkadaşına ona aşık olduğunu söyle.","Sürahiden su iç ve fotoğraf at.",
	"En çok konuştuğun karşı cinsten arkadaşına \" `Seni çok seviyorum galiba aşık oldum`\" yaz ve tepkisini bizimle paylaş",
	"İsmini 1 saatliğine Abdül<ismin> yap. (örneğin adın Berk ise AbdülBerk yap)","İnstagram'da dm kutunu (mesajlar bölümü) ss al gruba at.",
	"Tanımadığın birisine şu cümleyi atıp sohbet başlat: \"`Aşkımızın suya düşeceğini bilseydim , balık olurdum`\"",
	"En komik fotoğrafını grupla paylaş.","Grupta üyeler kısmına gir 11. kişiye \"`Analar neler doğuruyor bee`\" diye ses at ve cevabını grupla paylaş.",
	"Tanımadığın birine şu mesajı at sonra cevabını grupla paylaş ➡️\n  \"`Bu mesaj özel bir frekansla gönderilmiştir. Zekilerde hafıza kaybı, aptallarda kısa sureli körlük ibnelerde de bir anlık gülümseme yapar!`\"",
	"@ yaz çıkan ilk kişiyi etiketle ve seni seviyorum yaz.","Tanımadığın birine \" `sanırım sana aşık oldum`\" diye mesaj at.",
	"Telegram hakkında kısmına \"`Babasının Prensesi`\" yaz 1 saat boyunca dursun.","Birine Sesli Öpücük At Ve Etiketle",
	"Telegramda son konuşmanı ss at.","🎀 ŞANSLI MESAJ🎊 Grupdan İstediğin Birinin Google/Youtube/İnstagram Arama Geçmişini İste",
	"Galerinin En Alttan 7. Fotosunu gönder",
	"Sonraki 3 tur boyunca şiveyle konuş. Farklı şivelere kayış olursa /zar Komutunu kullanarak 6 ya en cok yaklaşan oyuncu sana ceza verecek",
	"Üç çorba kaşığı acı salça (veya buna benzer bir şey) ye ve video ya al gruba at",
	"5 dakika boyunca oyundaki birinin evcil hayvanı olmasını isteyebilirsin.","Yeri yala Ve fotoğraf/videosunu gruba at",
	"/zar Komutunu kullanarak 6 ya en cok yaklaşan oyuncuya sosyal medya hesaplarından birini 5dk ver",
	"3 dakika boyunca bir ünlüyü taklit et.", "Birisi taklit edilen sanatçıyı tahmin edene kadar bir sanatçıyı taklit et",
	"Grubun ortaya koyduğu bir konu etrafında sekiz satır ve iki mısralık bir şiir yaz",
	"Oyundaki kişilerin ortak kararıyla gruptan birini öp ses atarak (ortak karar verilemezse /zar komutundan 1 e en yakın oyuncuyu öp).",
	"5 dakika boyunca oyundaki bir kişinin kölesi ol.", "Bir süpürgeyle veya paspas ile dans et ve videosunu at",
	"Gerçek aşkının kim olduğunu ilan et","Ağzını hareket ettirmeden baştan sona alfabeyi oku okurken video at", "Aklına gelen ilk kelimeyi hemen söyle.",
	"Oyundaki oyunculardan biri hakkında hikaye uydur", "15 saniye içerisinde sondan başa doğru alfabeyi oku okurken ses at", "Bir köpek gibi havla havlarken ses at",
	"Bir şarkıyı baştan sona söyle söylerken ses at","Çıktığın en kötü ve en iyi kişiyi açıkla.",
	"Bir dakika boyunca karşı cinsten biri gibi yürü.","Sevgiline atıp atabileceğin en acımasız mesajı gönder.","Oyunda yer alan her kişi hakkında bildiğin komik bir şey anlat.",
	"Ünlü restoranlardan birini ara ve menülerini öğrenirken dalga geç.","Eski bir şarkıyı aç ve onu taklit ederek söylemeye çalış söylerken ses at","1 tur boyunca farklı bir dilde konuş.",
	"Eski sevgiline mesaj at ve onu unutamadığını söyle.","2 tur boyunca “sen” kelimesini duyunca kuş gibi ses çıkart.",
	"Telefondaki tarayıcı geçmişini herkese göster.","Odadan birisi için satın alacakmış gibi iç çamaşırı araştırması yap."
]

anne_hoplatan = [
	"Telefonunda en son aradığın şey neydi?","Birisi kız arkadaşın / erkek arkadaşından ayrılmak için sana 1 milyon tl önerseydi, yapar mıydın?",
	"Bu grupda en az kimi seviyorsun ve neden?","Hiç sınıfta yüksek sesle geğirdin mi?",
	"Hiç sınıfta yüksek sesle geğirdin mi?","Yerden bir şeyi alıp hiç yedin mi?",
	"Bir gün karşı cins olarak uyanırsan, ilk yapacağın şey nedir?",
	"Hiç havuzda işedin mi?","Asansörde hiç gaz kaçırdın mı?",
	"Tuvalette otururken aklınıza gelen şeyler nelerdir?","Büyüyen hayali bir arkadaşınız var mıydı?",
	"En kötü alışkanlığınız nedir?","Burnunu karıştırır mısın?","Banyoda şarkı söyler misin?",
	"Hiç üzerine işedin mi?","Toplumda en utanç verici anınız neydi?","Aynada kendinle hiç konuştun mu?",
	"Web geçmişinizi, birileri görürse utanacağınız şey ne olurdu?","Uykunda konuşur musun?",
	"Gizli aşkın kim?","Benim hakkımda neyi sevmiyorsun?","Şu an ne renk iç çamaşır giyiyorsun?",
	"Son attığın mesaj neydi?","İnsanları yanan bir binadan kurtarıyor olsaydınız ve bir kişiyi bu grupdan geride bırakmak zorunda kalırsanız, kim olurdu?",
	"İç çamaşırlarını ne sıklıkla yıkıyorsun?","Hiç kulak kiri tattın mı?",
	"Hiç osurup başka birini suçladın mı?","Hiç terinin tadına baktın mı?",
	"Bu odadaki kim bugüne kadarki en kötü insan olurdu? Neden?",
	"Yeniden doğmuş olsaydın, hangi yüz yılda doğmak isterdin?","Söylediğiniz veya yaptığınız bir şeyi silmek için zamanda geriye gidebilseydiniz, bu hangi yıl olurdu?",
	"Erkek arkadaşın veya kız arkadaşın seni hiç utandırdı mı?","Birdenbire görünmez olsaydın ne yapardın?",
	"Banyoda kaldığınız en uzun süre nedir ve neden bu kadar uzun süre kaldınız?","Şimdiye kadar gördüğüm en garip rüyayı anlat.",
	"Duşta işiyor musun?","Hala yaptığın en çocukça şey nedir?","Hangi çocuk filmini tekrar tekrar izleyebilirsin?",
	"Ayak kokunuz kötü mü?","Saçma takma adların var mı?","Telefonunuzda hangi uygulamada en çok zaman harcıyorsunuz?",
	"Tek bir oturuşta yediğin en çok yemek ne?","Tek başınayken dans ediyor musun?","Karanlıktan korkar mısın?",
	"Bütün gün evdeysen ne yapardın?","Günde kaç öz çekim yapıyorsunuz?","En son ne zaman dişlerini fırçaladın?",
	"En sevdiğin pijamalar neye benziyor?","Hiç yerden bir şey yedin mi?","Yapmaman gereken bir şeyi yaparken hiç yakalandın mı?",
	"Vücudunun hangi bölümünü seviyorsun, hangi kısmından nefret ediyorsun?","Hiç bitlendin mi?",
	"Pantolonunu hiç kestin mi?","Tabağını yalıyor musun?","Kimsenin senin hakkında bilmediği bir şey nedir?",
	"Hiç tabağını yaladın mı?","Dirseğini yalayabilir misin?","Eğer buradaki herkesi yanan bir binadan kurtarmaya çalışıyor olsaydın ve birini geride bırakmak zorunda kalırsan, kimi geride bırakırdın?",
	"Telefonda aradığın son şey neydi?","Bir uygulamayı telefonunuzdan silmek zorunda kalsanız hangisini silerdiniz?","Bir ilişkideki en büyük korkun nedir?",
	"Odanın her bir kişi hakkında bir tane olumlu, bir tane olumsuz şey söyleyin.","Sevmediğin kötü huyun var mı?",
	"Hayatında yaptığın en çılgın şey nedir?","Üç gün boyunca bir adada mahsur kalmış olsaydınız, bu grupdan kimleri seçerdiniz?",
	"Bu odadaki en sinir bozucu kişi kim?","Bu grupdan biriyle evlenmek zorunda kalsan kim olurdu?","En uzun ilişkiniz ne kadar sürdü?",
	"Bir ünlü Instagram’da seni takip etseydi bu ünlünün kim olmasını isterdin?","Instagram’da 5 kişiyi silmek zorunda olsan kimleri silerdin?",
	"Kaç çocuk sahibi olmak istersin?","Hayallerinizdeki kişiyi tarif edin.","Messi mi Ronaldo mu?","Pes mi Fifa mı?",
	"İlk işin neydi?","Üniversite hakkındaki en büyük korkun nedir?","En iyi arkadaşının seninle aynı üniversiteye gitmesini ister misin?",
	"Mevcut erkek arkadaşının ya da kız arkadaşının seninle aynı üniversiteye gitmesini ister misin?","Hayalindeki iş ne?",
	"Hiç bir dersten başarısız oldun mu?","Hiç kopya çektin mi?","Hiç sınıfta uyudun mu?","Sınıfta asla yanında oturmak istemeyeceğin kim?",
	"Derse hiç geç kaldın mı?","Bir öğretmenin önünde yaptığın en utanç verici şey nedir?","Hiç masanın altına sakız attın mı?",
	"Hiç okulda kavga ettin mi?","Bir sınavdan aldığın en kötü puan neydi?","Sınıfta hiç uyuya kaldın mı?","Hiç gözaltına alındın mı?",
	"Eğer görünmez olsaydın hangi derse gizlice girerdin?","En kötü grup hangisidir?","Bu grupdaki sır tutma  konusunda en çok zorlanan kişi kimdir?",
	"Söylediğin en son yalan neydi?","Spor yapar mısın?","Hayatının geri kalanında sadece bir kıyafet giyebilseydin, bu kıyafetin hangi renk olurdu?",
	"Sizce Türkiye’nin eğitim sisteminde yapılması gereken en önemli değişiklik nedir?","Karanlıktan/yükseklikten korkar mısın?",
	"Kendi görünuşünü 1 ile 10 arasında puanla :)","Yaptıgın en yasadışı şey neydi?","Şimdi sana bir evlenme teklifi gelse ve sevmediğin biri olsa, ve bu sana son gelecek evlilik teklifi olsa kabul edermiydin?",
	"Şu anki ruh haline bakarak ne tür film izlersin (aksiyon/dram/bilim kurgu/romantik komedi/biyografi/fantastik)",
	"Kendini en ezik hissettiğin an hangisiydi ?","ilerde çocuğun olursa ne isim koymak istersin?",
	"Unicorun mu olmasını isterdin ejderhan mı?","Kaç sevgilin oldu?","Hayatta unutmadığın biri var mı?",
	"en sevdiğin şarkı?","Yapmaman gereken bir şeyi yaparken hiç yakalandın mı?","En sevdiğin sanatçı kim?",
	"karşı cinste ilk dikkatini çeken ne?","bu yıl hayatında neyi değişmeyi uygun görüyorsun?",
	"Birinin telefonunda gördüğün en tuhaf şey nedir?","Süper kahramanlar gerçekten var olsaydı Dünya nasıl bir yer olurdu?",
	"Hayatın size öğrettiği en önemli ders nedir?","Kültürümüzün en çok sevdiğiniz yanı nedir?","Ailenizin uyguladığı en tuhaf gelenek nedir?",
	"Aileniz dışında, yaşamınız üzerinde en büyük etkisi olan kişi kimdir?","Kadın/Erkek olmanın en kötü ve en iyi yanı nedir?",
	"Beynini bir robota yerleştirebilir ve sonsuza kadar bu şekilde yaşayabilsedin,bunu yapar mıydın?","Evinizde ağırladığın en kötü misafir kimdi ve ne oldu?",
	"İnsanların size ne sormasından bıktınız?","En tuhaf korkunuz nedir?","En sevdiğiniz TV programı hangisidir?","Girdiğiniz en saçma tartışma nedir?",
	"En son söylediğin yalan nedir?", "Biriyle çıkarken yaptığın en utanç verici şey neydi?",
	"Hiç arabanla (varsa) yanlışlıkla bir şeye birine çarptın mı?",
	"Hoşuna gittiğini düşündüğün ama bir türlü açılamadığın biri oldu mu?","En tuhaf takma adın nedir?",
	"Fiziksel olarak sana en acı veren deneyimin ne oldu?","Hangi köprüleri yakmak seni rahatlattı?",
	"Toplu taşıma araçlarında yaptığın en çılgınca şey neydi?","Şişeden bir cin çıksa üç dileğin ne olurdu?","Dünyadaki herhangi birini Türkiye’nin başkanı yapabilseydin bu kim olurdu?",
	"Şimdiye kadar bir başkasına söylediğin en acımasızca şey neydi?","Birini öperken kendini hiç kötü hissettin mi?","Hiçbir sonucu olmayacağını bilsen ne yapmak isterdin?",
	"Bir aynanın önünde yaptığın en çılgınca şey nedir?","Şimdiye kadar başkasına söylediğin en anlamlı şey neydi?",
	"Arkadaşlarınla yapmayı sevdiğin ama sevgilinin önünde asla yapmayacağın şey nedir?","Bu hayatta en çok kimi kıskanıyorsun?",
	"En sevdiğin pijamaların neye benziyor?","Bir buluşmadan kaçmak için hiç hasta numarası yaptın mı?","Çıktığın en yaşlı kişi kim?",
	"Günde kaç tane özçekim yaparsın?","Aşk için her şeyi yaparım ama “bunu” yapmam dediğin şey nedir?","Haftada kaç kez aynı pantolonu giyiyorsun?",
	"Bugün şansın olsa lise aşkınla çıkar mısın?","Vücudunun hangi bölümlerinden gıdıklanıyorsun?",
	"Çeşitli batıl inançların var mı? Varsa onlar neler?","Sevdiğini itiraf etmekten utandığın film hangisidir?","En utan verici kişisel bakım alışkanlığın nedir?","En son ne zaman ve ne için özür diledin?","Sözlü destanlar hakkında ne düşünüyorsun?",
	"Utanç verici kokularınızın çoğu nereden geliyor?","Hiç sevgilini anlatmayı düşündün mü?","Hiç sevgilini biriyle aldattın mı?","Boxer mı yoksa külot mu?","Hiç havuza veya denize işedin mi?","Saçlarını uzatmayı düşünsen ne kadar uzatırdın?","Kimsenin bilmeyeceği garanti olsa kimi öldürmek isterdin?","Başkası için aldığın en ucuz hediye nedir?",
	"Zamanının çoğunu en çok hangi uygulamada harcıyorsun?","Otobüste yaptığın en tuhaf şey nedir?","Hiç toplum içinde çıplak kaldın mı?","Günde ne kadar dedikodu yaparsın?","Çıkmak isteyeceğin en genç kişi kaç yaşında olurdu?","Hiç toplum içindeyken burnunu karıştırdın mı?",
	"Hiç yaşın hakkında yalan söyledin mi?","Telefonundan bir uygulamayı silmek zorunda olsan bu hangisi olurdu?",
	"Gece geç saatte yaptığın en utanç verici şey nedir?","Duş almadan en uzun süre ne kadar durdun?","Hiç sahte kimlik kullandın mı?","Kırmızı halıda beraber yürümek istediğin ünlü isim kim?","Gizli aşkın kim?"
]

sikişenler = [
    "En son ne zaman mastürbasyon yaptın?",
    "Hayalindeki fantezi nedir?",
    "Bir gecelik ilişki yaşadın mı?",
    "Şu an biriyle sevişmek isteseydin, kim olurdu?",
    "Porno izliyor musun? En sevdiğin kategori?",
    "Hiç aynı cinsiyetten birine ilgi duydun mu?",
    "En utandığın cinsel deneyimin neydi?",
    "Şu an iç çamaşırı giyiyor musun?",
    "En garip yerde ilişkiye girdin mi?",
    "İlk öpüşmeni anlat.",
    "En çok tahrik olduğun şey ne?",
    "Hiç öğretmeninle ilgili fantazi kurdun mu?",
    "Şu an biriyle seks yapmak için teklif alsan kabul eder misin?",
    "Seks sırasında konuşur musun yoksa sessiz misin?",
    "Hiç cinsel içerikli rüya gördün mü?",
    "O rüyada kim vardı?",
    "Hiç arkadaşının sevgilisine ilgi duydun mu?",
    "Sevişirken sesli misin?",
    "En uzun süren ilişkisel deneyimin kaç dakika sürdü?",
    "Vajina/Penis hakkında en çok merak ettiğin şey nedir?",
    "Cinsel fantezilerin arasında en uçuk olanı hangisi?",
    "Seks oyuncakları kullanır mısın?",
    "Grup sekse açık mısın?",
    "Telefon seksi yaptın mı?",
    "En çok tahrik olduğun kelime nedir?",
    "Hiç çıplak poz gönderdin mi?",
    "Sana gönderilen en erotik mesaj neydi?",
    "Hiç karşı cinsten birine erotik mesaj attın mı?",
    "En çok hangi pozisyonu seviyorsun?",
    "Hiç aldatıldın mı?",
    "Hiç aldattın mı?",
    "İlk kez ne zaman seks yaptın?",
    "Hiç roleplay yaptın mı?",
    "Ayakta seks yaptın mı?",
    "Hiç duşta seks yaptın mı?",
    "Hiç dışarda seks yaptın mı?",
    "Hiç arabada seks yaptın mı?",
    "Hiç porno çektin mi?",
    "Seni en çok ne baştan çıkarır?",
    "En seksi bulduğun ünlü kim?",
    "Hiç partnerine bağırarak emir verdin mi?",
    "Hiç partnerin seni bağladı mı?",
    "Hiç gözlerin bağlı seviştin mi?",
    "Hiç biriyle sadece tek gecelik ilişki yaşadın mı?",
    "Hiç üçlü ilişki düşündün mü?",
    "Ayak fetişin var mı?",
    "Hiç oral seks yaptın mı?",
    "Hiç oral seks aldın mı?",
    "Hiç cinsel içerikli video izlerken yakalandın mı?",
    "Cinsel anlamda en utandığın an neydi?",
    "Hiç öğretmeninle flört ettin mi?",
    "En uzun süreli ereksiyon/ıslaklık yaşadığın an?",
    "Hiç anal seks yaptın mı?",
    "Seks sırasında uydurma sesler çıkarır mısın?",
    "Hiç erotik rüya görüp boşaldın mı?",
    "Bir gün boyunca çıplak gezmeyi ister miydin?",
    "Cinsel ilişki sırasında başına gelen komik bir olay?",
    "Seks esnasında müzik açar mısın?",
    "Hiç yasak ilişki yaşadın mı?",
    "Hiç bir akrabanla ilgili fantazi kurdun mu?",
    "Hiç sevgilinle halka açık bir yerde seviştin mi?",
    "Sana yapılan en iyi oral deneyimi anlat.",
    "Hiç seks yaparken yanlış ismi söyledin mi?",
    "Seks sırasında komik bir şey oldu mu?",
    "Hiç vibratör kullandın mı?",
    "Cinsel olarak seni en çok tahrik eden kıyafet?",
    "Hiç cinsel içerikli oyun oynadın mı?",
    "En kısa süren seks deneyimin kaç saniyeydi?",
    "Hiç kondom patladı mı?",
    "Hiç tek gecelik ilişkide ismini bilmediğin biriyle birlikte oldun mu?",
    "Hiç seks sırasında aniden gülme krizine girdin mi?",
    "Hiç telefonda seviştin mi?",
    "Seks sonrası ağladığın oldu mu?",
    "Hiç partnerin senden daha deneyimsiz oldu mu?",
    "Hiç bilinçli olarak sevişme ortamı hazırladın mı?",
    "Hiç tanımadığın biriyle mesajlaştın mı erotik anlamda?",
    "Hiç evli biriyle birlikte oldun mu?",
    "Hiç sosyal medyada erotik içerik paylaştın mı?",
    "Hiç çıplak yüzdün mü?",
    "Birine erotik ses kaydı gönderdin mi?",
    "Hiç yanlış kişiye erotik mesaj gönderdin mi?",
    "Partnerinle en uzun süre seviştiğin an kaç saatti?",
    "Hiç açık ilişki düşündün mü?",
    "Hiç cinsel ilişki sırasında yakalandın mı?",
    "Hiç sevgilinle cinsel anlamda uyumsuzluk yaşadın mı?",
    "Hiç partnerine seks yapmak istemediğini söyledin mi?",
    "Hiç seksi reddedildin mi?",
    "Hiç kıyafetli olarak seviştin mi?",
    "Hiç aynı anda iki kişiyle birlikte oldun mu?",
    "Sana yapılan en kötü cinsel hareket neydi?",
    "Hiç çıplak fotoğrafın sızdırıldı mı?",
    "Hiç yanlışlıkla erotik bir şey aile grubuna attın mı?",
    "Sence seks aşkı güçlendirir mi?",
    "Hiç biriyle sevişmek için buluşmaya gittin mi?",
    "Hiç sevgiline 'tatmin olmadım' dedin mi?",
    "Seni en çok tahrik eden söz neydi?",
    "Seks sırasında asla yapılmaması gereken şey nedir?",
    "Hiç porno izlerken başkasının ilgisini fark ettin mi?",
    "En çok sevdiğin ön sevişme türü?",
    "Hiç partnerinle erotik fantezi günlüğü tuttun mu?",
    "Cinsel anlamda denemek isteyip de denemediğin şey?",
    "Cinsel ilişki sonrası ilk yaptığın şey genelde nedir?",
]

erkeknude = [
    "https://i.hizliresim.com/q7sxgeu.jpg",
    "https://i.hizliresim.com/bqkmu2d.jpg",
    "https://i.hizliresim.com/ct3sgtl.jpg",
    "https://i.hizliresim.com/8vqyv0s.jpg",
    "https://i.hizliresim.com/5dm1e3j.jpg",
    "https://i.hizliresim.com/ctsumxf.jpg",
    "https://i.hizliresim.com/2vk3beh.jpg",
    "https://i.hizliresim.com/mlenj3v.jpg",
    "https://i.hizliresim.com/8bis432.jpg",
    "https://i.hizliresim.com/soq1mdu.jpg",
    "https://i.hizliresim.com/m03iaak.jpg",
    "https://i.hizliresim.com/g6lysqo.jpg",
    "https://i.hizliresim.com/d8ddxls.jpg",
    "https://i.hizliresim.com/7koiv3l.jpg",
    "https://i.hizliresim.com/owq0bkl.jpg",
    "https://i.hizliresim.com/gx3ylpz.jpg",
    "https://i.hizliresim.com/1kqxfyt.jpg",
    "https://i.hizliresim.com/a2kdwz6.jpg",
    "https://i.hizliresim.com/hx4awxs.jpg",
    "https://i.hizliresim.com/edoee9b.jpg"
]

@bot.on_message(filters.command("erkeknude"))
async def amk(_, message: Message):
    if erkeknude:
        yarra = random.choice(erkeknude)
        await message.reply_photo(photo=yarra)
    else:
        await message.reply("erkek nude listesi boş.")

fakekiz = [
    "https://telegra.ph/file/c69daf6d119d90d7c1d8f.jpg",
    "https://telegra.ph/file/d7eafb14a3294a49c9ed0.jpg",
    "https://telegra.ph/file/8104aa15fe751af206c14.jpg",
    "https://telegra.ph/file/ca478de4b507f44f9ec54.jpg",
    "https://telegra.ph/file/03aa11fdd46f96c410f5d.jpg",
    "https://telegra.ph/file/70deaa6256cd9d6d86e89.jpg",
    "https://telegra.ph/file/b19d6daa4a616f788f45d.jpg",
    "https://telegra.ph/file/0cfcc2206616995bada81.jpg",
    "https://telegra.ph/file/0cfcc2206616995bada81.jpg",
    "https://telegra.ph/file/65a290bf8e6df370762a8.jpg",
    "https://telegra.ph/file/78951fe3c499cc7433961.jpg",
    "https://telegra.ph/file/889781c7d2fb5bd1d3f2c.jpg",
    "https://telegra.ph/file/ad59bcf4bc0840909ce0c.jpg",
    "https://telegra.ph/file/8a2366094ee43e18c873b.jpg",
    "https://telegra.ph/file/97d00a1bea9094b9cd0c6.jpg",
    "https://telegra.ph/file/df1408d0293d55ddc867b.jpg",
    "https://telegra.ph/file/86a3020627709ee3b79b8.jpg",
    "https://telegra.ph/file/dc01b73c7b8c5b84c0ceb.jpg",
    "https://telegra.ph/file/ff705236..."
]

@bot.on_message(filters.command("fakekiz"))
async def amolduren(_, message: Message):
    if fakekiz:
        am = random.choice(fakekiz)
        await message.reply_photo(photo=am)
    else:
        await message.reply("fake kiz listesi boş.")

@bot.on_message(filters.command("eros") & filters.group)
async def yarrabeni(_, message: Message):
    ramazan = []

    async for m in bot.get_chat_members(message.chat.id):
        if m.user and not m.user.is_deleted and not m.user.is_bot:
            ramazan.append(m.user)

    if len(ramazan) < 2:
        await message.reply("Uyum için grupta yeterli kullanıcı yok 😢")
        return

    amcik, yarrak = random.sample(ramazan, 2)

    uyum = random.randint(50, 100)

    if uyum >= 90:
        kalpler = ["💘", "💖", "💝", "❤️"]
    elif uyum >= 80:
        kalpler = ["💗", "💕", "💞"]
    elif uyum >= 70:
        kalpler = ["💓", "💛", "🧡"]
    elif uyum >= 60:
        kalpler = ["💙", "💚", "💜"]
    else:
        kalpler = ["🖤", "🤍", "🤎"]

    kalp = random.choice(kalpler)

    ramoş = f"""
🏹 Eros'un Oku Atıldı 🏹

[{amcik.first_name}](tg://user?id={amcik.id}) {kalp} [{yarrak.first_name}](tg://user?id={yarrak.id})

💫 Uyum: %{uyum}
"""

    await message.reply(ramoş)

kiznude = [
    "https://i.hizliresim.com/8izxfrw.jpg",
    "https://i.hizliresim.com/j7ra38k.jpg",
    "https://i.hizliresim.com/im6z0p8.jpg",
    "https://i.hizliresim.com/d0jkr9h.jpg",
    "https://i.hizliresim.com/f8ipx54.jpg",
    "https://i.hizliresim.com/krwkats.jpg",
    "https://i.hizliresim.com/ru6e1t7.jpg",
    "https://i.hizliresim.com/9rh8cqk.jpg",
    "https://i.hizliresim.com/niknsnm.jpg",
    "https://i.hizliresim.com/f8lafes.jpg",
    "https://i.hizliresim.com/5lrphg0.jpg",
    "https://i.hizliresim.com/fwt6hoy.jpg",
    "https://i.hizliresim.com/latjqar.jpg",
    "https://i.hizliresim.com/aorap9b.jpg",
    "https://i.hizliresim.com/jwdq5zt.jpg",
    "https://i.hizliresim.com/qzi11kn.jpg",
    "https://i.hizliresim.com/dr5wbwa.jpg",
    "https://i.hizliresim.com/a218xjo.jpg",
    "https://i.hizliresim.com/hmmm88m.jpg",
    "https://i.hizliresim.com/jdo7z3f.jpg",
    "https://i.hizliresim.com/tie94rc.jpg",
    "https://i.hizliresim.com/47bvdtm.jpg"
    "https://i.hizliresim.com/rbnnwrl.jpg"
    "https://i.hizliresim.com/7j5ebip.jpg"
]

@bot.on_message(filters.command("kiznude"))
async def amcikyenirp(_, message: Message):
    if kiznude:
        foto = random.choice(kiznude)
        await message.reply_photo(photo=foto)
    else:
        await message.reply("Kiznude listesi boş.")

@bot.on_message(filters.command("ifsa"))
async def am_severim(_, message):
    await message.reply(
        "🌟 İfşa Menüsüne Hoşgeldin\n\nAşağıdaki Butonları Kullanarak Bir Ünlü Seç 👇",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("💦 Melek Azad", url="https://ay.live/QcUj"), InlineKeyboardButton("🔥 Aleyna Tilki", url="https://ay.live/yb0NQ")],
            [InlineKeyboardButton("🔱 Ece Seçkin", url="https://ay.live/pi8T"), InlineKeyboardButton("😈 Gizem Savage", url="https://ay.live/zQI8C")],
            [InlineKeyboardButton("👅 Hande Erçel", url="https://ay.live/vi42TN"), InlineKeyboardButton("🥵 Elanur Pat", url="https://ay.live/ekMd")],
            [InlineKeyboardButton("💋 Simge Barankoğlu", url="https://ay.live/kg5wW3"), InlineKeyboardButton("🐤 Hadise", url="https://ay.live/TBqK")],
            [InlineKeyboardButton("🌟 Mia Khalifa", url="https://ay.live/Xj0D8"), InlineKeyboardButton("☘️ Billie Eilish", url="https://ay.live/IvIcOQ")],
            [InlineKeyboardButton("🥶 Ece Ronay", url="https://ay.live/c5gs"), InlineKeyboardButton("😍 Buse Korkmaz", url="https://ay.live/xK8vKS")],
            [InlineKeyboardButton("✨ Gözde Akgün", url="https://ay.live/6HG5QS"), InlineKeyboardButton("😻 Nurseli Aksoy", url="https://ay.live/A2I4yR")],
            [InlineKeyboardButton("❤️‍🔥 Hannah Owo", url="https://ay.live/2ioUy"), InlineKeyboardButton("👉 Porno Grubumuz", url="https://t.me/ramowlf")],
            [InlineKeyboardButton("❌ Kapat ❌", callback_data="kapat")]
        ])
    )

@bot.on_message(filters.command("dsor"))
async def teyzeni_sikerim(_, message):
    if anne_hoplatan:
        babacik = choice(anne_hoplatan)
        await message.reply(babacik)
    else:
        await message.reply("doğruluk listesi boş.")

@bot.on_message(filters.command("sor18"))
async def ohh_azdim(_, message):
    if sikişenler:
        gavatlar = choice(sikişenler)
        await message.reply(gavatlar)
    else:
        await message.reply("+18 listesi boş.")

@bot.on_message(filters.command("csor"))
async def anani_hoplatirim(_, message):
    if cokseksiyim:
        annecik = choice(cokseksiyim)
        await message.reply(annecik)
    else:
        await message.reply("cesaret listesi boş.")

@bot.on_message(filters.command("tekrarla"))
async def omega_sakso(_, message: Message):
    if len(message.command) < 2:
        await message.reply("❌ Hatalı Kullanım\n\n✅ Doğru Kullanım:\n\ntekrarla Benim Adım Alev")
    else:
        yarramiye = " ".join(message.command[1:])
        await message.reply(yarramiye)
        
@bot.on_message(filters.command("sovcular"))
async def azginlar(_, message: Message):
    ramom = """
✅ Onaylı Şovcular ✅

➺ @
➺ @
➺ @

🔴 Şovcuysan Ve Ücretsiz Reklam Yapmak İstiyorsan Bana Ulaş
"""
    ramazancik = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("💬 Reklam Ver 💬", url="https://t.me/ramowlf")]
        ]
    )

    await message.reply(ramom, reply_markup=ramazancik)

@bot.on_message(filters.command("start"))
async def  Instagram_ramowlf(_, message):
    gavat_oc = InlineKeyboardMarkup([
        [InlineKeyboardButton("🤔 Ne İşe Yarıyorum?", callback_data="komutlar")],
        [InlineKeyboardButton("🔞 İtiraf Kanalı 🔞", url="https://t.me/ramowlf")],
        [InlineKeyboardButton("🔥 Porno Grubu 🔥", url="https://t.me/ramowlf")],
        [InlineKeyboardButton("💋 Arayış Grubumuz 💋", url="https://t.me/ramowlf")],
        [InlineKeyboardButton("➕ Beni Gruba Ekle ➕", url="https://t.me/Gotunuyerimocbot?startgroup=true")]
    ])
    await message.reply(
        "♥️ **Merhaba Ben Alev**\n\n"
        "+18 Sohbet Botuyum 🔞\n"
        "Başlamak için beni **arayış** ya da **yetişkin bir gruba** ekleyip **yönetici** yap.\n",
        reply_markup=gavat_oc
    )

@bot.on_callback_query(filters.regex("komutlar"))
async def vayorospu(_, query):
    vay_oc = InlineKeyboardMarkup([
        [InlineKeyboardButton("⏪ Ana Menü ⏪", callback_data="anne_öldüren")]
    ])
    await query.message.edit(
    """➺ Onaylı Şovcular Listesi ( /sovcular )
➺ Ünlülerin İfşa Menüsünü ( /ifsa )
➺ Fake Kız Fotoğrafı Atar ( /fakekiz )
➺ Kız Nude Fotoğrafı Atar Atar ( /kiznude )
➺ Erkek Nude Fotoğrafı Atar Atar ( /erkeknude )
➺ +18 Sorusu Atar ( /sor18 )
➺ Doğruluk Sorusu Atar ( /dsor )
➺ Cesaret Sorusu Atar ( /csor )
➺ Eros Oku Atar ( /eros )
➺ Yazıyı Sese Çevirir ( /ses )
➺ Metni Tekrarlarım ( /tekrarla )
➺ Kullanıcıları Etiketler ( /utag )
➺ Adminleri Etiketler ( /atag )
➺ Etiket Durdurur ( /durdur )
➺ Grup Bilgisini Verir ( /info )""", reply_markup=vay_oc
    )

@bot.on_callback_query(filters.regex("anne_öldüren"))
async def orospu_evladi(_, query):
    amini_yerim = InlineKeyboardMarkup([
        [InlineKeyboardButton("🤔 Ne İşe Yarıyorum?", callback_data="komutlar")],
        [InlineKeyboardButton("🔞 İtiraf Kanalı 🔞", url="https://t.me/ramowlf")],
        [InlineKeyboardButton("🔥 Porno Grubu 🔥", url="https://t.me/ramowlf")],
        [InlineKeyboardButton("💋 Arayış Grubumuz 💋", url="https://t.me/ramowlf")],
        [InlineKeyboardButton("➕ Beni Gruba Ekle ➕", url="https://t.me/?startgroup=true")]
    ])
    await query.message.edit(
        "♥️ **Merhaba Ben Alev**\n\n"
        "+18 Sohbet Botuyum 🔞\n"
        "Başlamak için beni **arayış** ya da **yetişkin bir gruba** ekleyip **yönetici** yap.\n",
        reply_markup=amini_yerim
    )

@bot.on_message(filters.command("info"))
def amcik_isiririm(c, m):
  total = 0
  online = 0
  bots = 0
  deleted = 0
  if m.chat.type == ChatType.PRIVATE:
    return 
  for member in bot.get_chat_members(m.chat.id):
    total += 1
    if member.user.is_deleted:
      deleted += 1
    elif member.user.status == UserStatus.ONLINE:
      online += 1
    elif member.user.is_bot:
      bots += 1
  return m.reply(f"""
**ɢʀᴜᴘ ᴀᴅɪ :** `{m.chat.title}`
**ɢʀᴜᴘ ɪᴅ :** `{m.chat.id}`
**ᴀᴋᴛɪғ ᴜ̈ʏᴇʟᴇʀ :** `{online}`
**sɪ̇ʟɪ̇ɴᴇɴ ʜᴇsᴀᴘʟᴀʀ :** `{deleted}`
**ʙᴏᴛʟᴀʀɪɴ sᴀʏɪsɪ :** `{bots}`
**ᴛᴏᴘʟᴀᴍ ᴜ̈ʏᴇʟᴇʀ :** `{total}`
  """)

@bot.on_message(filters.new_chat_members)
def newmember(c, m):
  global tagging
  global tag_users
  global tag_text
  for member in m.new_chat_members:
    if member.id == bot.get_me().id:
      tagging[m.chat.id] = False
      tag_users[m.chat.id] = []
      tag_text[m.chat.id] = ""
      
@bot.on_message(filters.command("atag"))
async def atag(c, m):
    global tagging, tag_text

    if m.chat.id not in tagging:
        tagging[m.chat.id] = False
    if m.chat.id not in tag_text:
        tag_text[m.chat.id] = ""

    status = await bot.get_chat_member(m.chat.id, m.from_user.id)
    if status.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        return await m.reply("**ʏöɴᴇᴛɪᴄɪ ᴅᴇğɪʟsɪɴ 💀**")

    args = m.text.split()
    if len(args) < 2 and not m.reply_to_message:
        return await m.reply("**ᴇᴛɪᴋᴇᴛʟᴇᴍᴇᴍ ɪçɪɴ ʙɪʀ ᴍᴇᴛɪɴ ʙᴇʟɪʀᴛ ᴠᴇʏᴀ ʙɪʀ ᴍᴇsᴀᴊı ʏᴀɴıᴛʟᴀ 🤔**")

    if m.reply_to_message:
        tag_text[m.chat.id] = m.reply_to_message.text
    else:
        tag_text[m.chat.id] = ' '.join(args[1:])

    if tagging[m.chat.id]:
        return await m.reply("**ᴢᴀᴛᴇɴ ᴇᴛɪᴋᴇᴛʟᴇᴍᴇ ɪşʟᴇᴍɪ ᴀᴋᴛɪғ :)} 😁**")

    tagging[m.chat.id] = True

    user_count = 0
    text_chunk = ""
    async for member in bot.get_chat_members(m.chat.id, filter=ChatMembersFilter.ADMINISTRATORS):
        if not tagging.get(m.chat.id):  
            break
        if not member.user.is_deleted:
            try:
                await bot.send_message(m.chat.id, f"**{tag_text[m.chat.id]}**\n\n**{member.user.mention}**") 
                user_count += 1
                await asyncio.sleep(1)
            except Exception as e:
                print(f"Error sending message to {member.user.first_name}: {e}")

    tagging[m.chat.id] = False
    tag_text[m.chat.id] = ""
    return await m.reply("**ᴇᴛɪᴋᴇᴛʟᴇᴍᴇ ɪşʟᴇᴍɪ ᴛᴀᴍᴀᴍʟᴀɴᴅı ✅😃**")
    
@bot.on_message(filters.command("utag"))
async def tag(c, m):
    global tagging, tag_text
    if m.chat.id not in tagging:
        tagging[m.chat.id] = False
    if m.chat.id not in tag_text:
        tag_text[m.chat.id] = ""

    status = await bot.get_chat_member(m.chat.id, m.from_user.id)
    if status.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        return await m.reply("**Bu komutu sadece yöneticiler kullanabilir. ✋**")

    args = m.text.split()
    if len(args) < 2 and not m.reply_to_message:
        return await m.reply("**Etikete Başlamak için sebep yazın veya bir mesajı yanıtlayın. 🤔**")

    if m.reply_to_message:
        tag_text[m.chat.id] = m.reply_to_message.text
    else:
        tag_text[m.chat.id] = ' '.join(args[1:])

    if tagging[m.chat.id]:
        return await m.reply("**Etiket işlemi zaten aktif 😁**")

    tagging[m.chat.id] = True
    await m.reply("✅ **Etiketleme başlatıldı...**")

    user_count = 0
    text_chunk = ""
    async for user in bot.get_chat_members(m.chat.id):
        if not tagging.get(m.chat.id):  
            break
        if user.user.is_bot or user.user.is_deleted:
            continue
        text_chunk += f"[{user.user.first_name}](tg://user?id={user.user.id}), "
        user_count += 1
        if user_count == 5:
            try:
                await bot.send_message(m.chat.id, f"**{tag_text[m.chat.id]}**\n\n{text_chunk}")
            except:
                pass
            await asyncio.sleep(2)
            user_count = 0
            text_chunk = ""

    tagging[m.chat.id] = False
    tag_text[m.chat.id] = ""
    return await m.reply("**✅ Etiketleme tamamlandı.**")
 
@bot.on_message(filters.command("cancel"))
async def cancel(c, m): 
  status = await bot.get_chat_member(m.chat.id, m.from_user.id)
  if status.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
    return await m.reply("**ʏöɴᴇᴛɪᴄɪ ᴅᴇğɪʟsɪɴ 💀**") 
  tagging[m.chat.id] = False
  return await m.reply("**ᴇᴛɪᴋᴇᴛʟᴇᴍᴇ ɪşʟᴇᴍɪ ɪᴘᴛᴀʟ ᴇᴅɪʟᴅɪ ✅**")
    
@bot.on_message(filters.command("ses"))
def ramazaninyarra(client, message: Message):
    metin = "botumuzu kullandığınız için teşekkür ederiz"
    
    if len(message.command) > 1:
        metin = " ".join(message.command[1:])

    message.reply_text("🔊 **Metin sese çevriliyor...**")

    try:
        tts = gtts.gTTS(metin, lang="tr")
        dosya_adi = f"ses_{random.randint(1000, 9999)}.mp3"
        tts.save(dosya_adi)

        client.send_voice(message.chat.id, voice=dosya_adi)
        os.remove(dosya_adi)

    except Exception as e:
        message.reply_text(f"❌ Hata oluştu, @ramowlf ile iletişime geçin:\n\n**{str(e)}**")
  
if True:
  print(f"Bot {bot.get_me().first_name} adıyla başlatıldı.")
  idle()