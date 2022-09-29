# DataScrappingWithPython
Python - Selenium kütüphanesi ile nasıl Veri Kazıma yapılır hadi gelin hep birlikte bakalım.
Veri kazıma işlemleri otomasyon ürünlerinde her zaman sıklıkla kullanılan aktivitelerin başında gelmiştir. UI Path ile yaptığım projelerin neredeyse her birinde bir “Veri Kazıma” aktivitesi kullanıyorum. Peki bu veri kazıma işlemini herhangi bir otomasyon ürünü kullanmadan, ücretsiz bir şekilde yapmak istersem durağım neresi olacak?

Bu konudaki sorularımı Guuugıllarken kendimi bir Python kütüphanesi olan “Selenium” gönderilerinin içerisinde buldum. Her python geliştiricisi en az bir kez bu kütüphanenin ismini duymuştur ve ne işe yaradığını da araştırmıştır. Peki bu kütüphaneyi neden kullanıyoruz? Ve Selenium nedir?

# Selenium

Selenium, farklı tarayıcılarda web uygulamalarını test etmek için kullanılan açık kaynaklı ve ücretsiz test aracıdır. Kendini tekrar eden işlemlerin manuel olarak yapıldığında ortaya çıkan ekstra iş yükünü ortadan kaldırarak, süreci otomatikleştirmek ve zaman kazanmamızı sağlamaktır. Aslında burada otomasyonların ortaya çıkış sebebini de bir nevi açıklamış olduk. Bu işlemleri gerçekleştirirken Python, Java, Ruby, .Net, C# gibi birden fazla programlama dili kullanabilirsiniz. Ben bu yazımda sizlere Python üzerinden örnek vermeye çalışacağım.

İl olarak Selenium paketimizi Python programımıza dahil edelim.

![image](https://user-images.githubusercontent.com/63015101/192955597-e4d2f4ce-773c-437c-82a0-512f8e3194cf.png)

Tarayıcı üzerinde sayfa açmak istediğimizde kullandığımız tarayıcıda kasma sorunları olabileceği ihtimalini düşünerek Time paketini Python programımıza ekliyoruz.

![image](https://user-images.githubusercontent.com/63015101/192955704-349e3695-b435-4a49-804e-c258dc9c29ca.png)

Son olarak kazıdığımız verileri bir tabloya dönüştürüp Excel’e yazdırmak için Pandas paketini Python programımıza ekliyoruz.

![image](https://user-images.githubusercontent.com/63015101/192955748-480b732a-442f-4542-b560-676c531bc6f4.png)

Driverimizi tanımlıyoruz ve browser öğemizi oluşturuyoruz. Ben bu uygulamada Chrome Driver kullanacağım.

![image](https://user-images.githubusercontent.com/63015101/192955832-700d88cb-942f-4110-8868-8683824b8540.png)

WorldoMeters.info adresi “url” değişkenine tanımlanır ve -browser.get(url)- ile Chrome açılır. Ardından tarayıcının beklemesi/kasması ihtimalini göze alarak 5 saniyelik bekleme yapılır(-time.sleep(5)-). Açılan tarayıcı -browser.maximize_window()- ile tam ekran yapılır.

![image](https://user-images.githubusercontent.com/63015101/192955898-7bf1c1d9-d049-47cd-8faa-02af78ca3bff.png)

*****

Paketlerimizi yükledik ve tarayıcımızı başlattık. Artık dışarı aktarmak istediğimiz veriyi WorldoMeters.info adresinden inceleyebiliriz.

![image](https://user-images.githubusercontent.com/63015101/192956015-cb9499da-fce7-40b5-a20e-75d05a233b39.png)

Burada görmüş olduğunuz liste hem ülkeleri hem de bağımlı bölgeleri içermektedir. Birleşmiş milletlere ait olan ve son hali olan Birleşmiş Milletler Nüfus Bölümü tahminine dayanan veriler kullanılmaktadır. Burada almak istediğimiz veriler sırasıyla Country, Population, Yearly Change, Net Change verileridir. Selenium bizlere farklı methodlar ile sayfa kaynağından veri çekmemize olanak sağlıyor. Ben bu uygulamamda “By.XPATH” ile verilerimi kazımaya çalışacağım. Sayfa üzerinde herhangi bir yere sağ tık ile tıklayarak “incele” seçeneğine tıklıyoruz.

![image](https://user-images.githubusercontent.com/63015101/192956208-35004062-668b-4e3d-bd51-af71e7bb93cb.png)

İncele seçeneğine tıkladıktan sonra ilgili tabloyu seçiyoruz ve sayfa kaynağındaki yerini görüntülüyoruz.

![image](https://user-images.githubusercontent.com/63015101/192956244-f7305a5b-b139-4de6-9ccb-7b87e43f96f9.png)

Almak istediğimiz ilk veri olan Country bilgisi için sayfa kaynağında ilgili kolonun XPATH’ini kopyalıyoruz.
(Örnek çıktı: //*[@id=”example2"]/thead/tr/th[2])

![image](https://user-images.githubusercontent.com/63015101/192956456-fde509db-5dcc-452d-8070-174cf2cdf46d.png)

Şimdi kopyaladığımız XPATH’leri kod içerisinde düzenleyelim.

*****

Yukarıda da bahsettiğim gibi Selenium bize farklı yollarla istediğimiz verileri almamızı sağlamaktadır. Find_elements(By.XPATH,”Kopyalamış olduğumuz XPATH”) ile ilgili kolonun XPATH’ini tanımlıyoruz.

![image](https://user-images.githubusercontent.com/63015101/192956861-8caeb1a0-39ee-4af1-9974-46e08b103956.png)

Ardından dışarı almış olduğumuz veriler için bir döngü oluşturuyoruz ve “Kolon Adı : Veri” tipinde bir Dictionary oluşturuyoruz. Oluşturmuş olduğumuz Dictionary öğesini “total_result” değişkenine ekliyoruz. Bu eklediğimiz verileri bir sonraki adımımızda bir Excel dosyasına yazdıracağız.

![image](https://user-images.githubusercontent.com/63015101/192956920-4ea6366a-a4d8-4128-acaf-f1ba49c22567.png)

Artık son adımımız olan Excel’e yazdırma adımına geliyoruz ve burada Pandas kütüphanesinin bir sınıfı olan ExcelWriter ile oluşturacağımız dataframe’yi bir Excel dosyasına yazdıracağız. Az önce bir array içerisine eklediğimiz Dictionary’leri pd.DataFrame ile Data Frame içerisine alıyoruz. Son olarak Excel Writer ile Sheet Name = sheet1 olan ve içerisinde index içermeyen bir Excel’e verilerimizi yazdırıyoruz.

![image](https://user-images.githubusercontent.com/63015101/192956972-3cd7677c-e1b2-4921-98ec-10c78fe6814d.png)

Ve dışarı aktarmış olduğumuz verilerimiz bu şekilde gözükmektedir.

![image](https://user-images.githubusercontent.com/63015101/192957032-ed651fa9-3b72-48bc-b252-d3d677b130e4.png)

*****

Bu yazımda sizlere Python programlama dilinde Selenium kütüphanesini kullanarak bir web sitesi içerisinden nasıl veri kazıma yapılır bunu anlatmaya çalıştım. Bu noktaya kadar sabredip inceleyip-okuduğunuz için teşekkür ederim.
