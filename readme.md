AI Image Detection
Bu proje, yapay zeka (YZ) tarafından üretilen görselleri insan yapımı görsellerden ayırt etmek amacıyla geliştirilmiştir. Görsel içeriklerin güvenilirliği, özellikle gazetecilik, hukuk ve sosyal medya alanlarında büyük önem taşımaktadır. Bu nedenle, YZ tarafından oluşturulan görsellerin tespiti giderek daha kritik hâle gelmektedir.

🔍 Projenin Amacı
Gelişen yapay zeka teknolojileri sayesinde, insan gözüyle ayırt edilmesi güç derecede gerçekçi görseller üretilebilmektedir. Bu proje, bu tür yapay görselleri güvenilir bir şekilde tespit edebilecek bir sınıflandırma sistemi oluşturmayı hedeflemektedir.

🧠 Kullanılan Model: AIDE (Geliştirilmiş Sürüm)
Projede temel olarak AIDE (AI-generated Image DEtector with Hybrid Features) modeli kullanılmıştır. Ancak, proje geliştirilirken orijinal AIDE mimarisi üzerinde bazı önemli değişiklikler yapılmıştır:

Yapılan Değişiklik: Orijinal AIDE modelinde kullanılan yüksek frekans (high-frequency) bileşeni çıkarılarak yerine korelasyon farkı yöntemi (correlation difference method) entegre edilmiştir. Bu değişiklik, modelin görsel yapaylık sinyallerini daha hassas şekilde analiz etmesini sağlamıştır.

Modelin Avantajı: AIDE, hem doğal hem de yapay içerikler üzerinde yüzeysel ve yapısal farklılıkları analiz edebilen hibrit özellikleriyle dikkat çeker. Korelasyon farkı yöntemi ile görsellerdeki yapaylık izleri daha belirgin şekilde ortaya konulabilmiştir.

👨‍💻 Geliştiriciler
İhsan Kayacı

Ali Berkay Taşbölen

🗂️ Proje Yapısı
bash
Kopyala
Düzenle
AI-image-detection/
├── data/                  # Ham veri dosyaları
├── dataset/               # İşlenmiş veri setleri
├── docs/                  # Dokümantasyon dosyaları
├── models/                # Eğitilmiş model ağırlıkları
├── scripts/               # Eğitim ve test betikleri
├── engine_finetune.py     # Model ince ayar motoru
├── main_finetune.py       # Ana eğitim betiği
├── optim_factory.py       # Optimizasyon ayarları
├── utils.py               # Yardımcı fonksiyonlar
├── requirements.txt       # Gerekli Python paketleri
└── LICENSE                # MIT Lisansı
⚙️ Kurulum
Depoyu Klonlayın:

bash
Kopyala
Düzenle
git clone https://github.com/Palakonik/AI-image-detection.git
cd AI-image-detection
Gerekli Paketleri Yükleyin:

bash
Kopyala
Düzenle
pip install -r requirements.txt
Modeli Eğitin veya Test Edin:

Eğitim:

bash
Kopyala
Düzenle
python main_finetune.py
Test:

bash
Kopyala
Düzenle
python engine_finetune.py
📊 Sonuçlar
Güncellenmiş AIDE modeli ile yapılan testlerde, YZ tarafından üretilen görsellerin tespiti konusunda yüksek doğruluk oranlarına ulaşılmıştır. Korelasyon farkı yönteminin entegre edilmesiyle modelin genel başarımı önemli ölçüde artmıştır.

📄 Lisans
Bu proje MIT Lisansı ile lisanslanmıştır.

🙏 Katkılar
Projeye katkıda bulunan tüm geliştiricilere ve orijinal AIDE modelinin yaratıcılarına teşekkür ederiz.