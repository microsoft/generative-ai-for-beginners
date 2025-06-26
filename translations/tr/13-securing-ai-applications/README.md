<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f3cac698e9eea47dd563633bd82daf8c",
  "translation_date": "2025-06-25T21:13:19+00:00",
  "source_file": "13-securing-ai-applications/README.md",
  "language_code": "tr"
}
-->
# Üretken AI Uygulamalarınızı Güvenli Hale Getirme

## Giriş

Bu ders şunları kapsayacak:

- AI sistemleri bağlamında güvenlik.
- AI sistemlerine yönelik yaygın riskler ve tehditler.
- AI sistemlerini güvenli hale getirme yöntemleri ve dikkate alınması gerekenler.

## Öğrenme Hedefleri

Bu dersi tamamladıktan sonra, aşağıdaki konularda bilgi sahibi olacaksınız:

- AI sistemlerine yönelik tehditler ve riskler.
- AI sistemlerini güvenli hale getirmek için yaygın yöntemler ve uygulamalar.
- Güvenlik testlerinin uygulanmasının beklenmedik sonuçları ve kullanıcı güveninin azalmasını nasıl önleyebileceği.

## Üretken AI bağlamında güvenlik ne anlama geliyor?

Yapay Zeka (AI) ve Makine Öğrenimi (ML) teknolojileri hayatımızı giderek daha fazla şekillendirirken, sadece müşteri verilerini değil, aynı zamanda AI sistemlerini de korumak çok önemlidir. AI/ML, yanlış kararın ciddi sonuçlara yol açabileceği sektörlerde yüksek değerli karar verme süreçlerini desteklemek için giderek daha fazla kullanılmaktadır.

Dikkate alınması gereken önemli noktalar şunlardır:

- **AI/ML'nin Etkisi**: AI/ML günlük yaşam üzerinde önemli etkilere sahiptir ve bu nedenle onları korumak zorunlu hale gelmiştir.
- **Güvenlik Zorlukları**: AI/ML'nin bu etkisi, troller veya organize gruplar tarafından yapılan sofistike saldırılardan AI tabanlı ürünleri koruma ihtiyacını ele almak için uygun dikkat gerektirir.
- **Stratejik Problemler**: Teknoloji sektörü, uzun vadeli müşteri güvenliğini ve veri güvenliğini sağlamak için stratejik zorlukları proaktif olarak ele almalıdır.

Ayrıca, Makine Öğrenimi modelleri büyük ölçüde kötü niyetli girdi ile zararsız anomalik veriyi ayırt edemez. Eğitim verilerinin önemli bir kaynağı, üçüncü taraf katkılarına açık olan düzensiz, denetlenmemiş, halka açık veri kümelerinden elde edilir. Saldırganlar, veri kümelerini değiştirmek zorunda kalmadan onlara katkıda bulunabilir. Zamanla, düşük güvenilirlikteki kötü niyetli veriler, veri yapısı/formatı doğru kaldığı sürece yüksek güvenilirlikte güvenilir verilere dönüşür.

Bu nedenle modellerinizin karar vermek için kullandığı veri depolarının bütünlüğünü ve korumasını sağlamak kritik önem taşır.

## AI'nın tehditlerini ve risklerini anlama

AI ve ilgili sistemler açısından, veri zehirlenmesi bugün en önemli güvenlik tehdidi olarak öne çıkmaktadır. Veri zehirlenmesi, birinin AI'yı eğitmek için kullanılan bilgileri kasıtlı olarak değiştirerek hatalar yapmasına neden olmasıdır. Bu, standart algılama ve hafifletme yöntemlerinin olmaması ve eğitim için güvenilmeyen veya düzensiz halka açık veri kümelerine olan bağımlılığımızdan kaynaklanmaktadır. Veri bütünlüğünü korumak ve kusurlu bir eğitim sürecini önlemek için verinizin kökenini ve soyunu takip etmek önemlidir. Aksi takdirde, "çöp girerse, çöp çıkar" atasözü geçerli olur ve model performansının tehlikeye girmesine yol açar.

Veri zehirlenmesinin modellerinizi nasıl etkileyebileceğine dair örnekler:

1. **Etiket Çevirme**: İkili sınıflandırma görevinde, bir düşman, eğitim verilerinin küçük bir alt kümesinin etiketlerini kasıtlı olarak çevirir. Örneğin, zararsız örnekler kötü niyetli olarak etiketlenir ve model yanlış ilişkiler öğrenir.\
   **Örnek**: Etiketlerin manipülasyonu nedeniyle bir spam filtresinin meşru e-postaları spam olarak yanlış sınıflandırması.
2. **Özellik Zehirlenmesi**: Bir saldırgan, modelin yanlı veya yanıltıcı öğrenmesini sağlamak için eğitim verilerindeki özellikleri ince bir şekilde değiştirir.\
   **Örnek**: Ürün açıklamalarına öneri sistemlerini manipüle etmek için alakasız anahtar kelimeler eklemek.
3. **Veri Enjeksiyonu**: Modelin davranışını etkilemek için eğitim setine kötü niyetli veri enjekte etme.\
   **Örnek**: Duygu analizi sonuçlarını çarpıtmak için sahte kullanıcı yorumları eklemek.
4. **Arka Kapı Saldırıları**: Bir düşman, eğitim verilerine gizli bir desen (arka kapı) ekler. Model bu deseni öğrenir ve tetiklendiğinde kötü niyetli davranır.\
   **Örnek**: Belirli bir kişiyi yanlış tanımlayan arka kapılı görüntülerle eğitilmiş bir yüz tanıma sistemi.

MITRE Corporation, AI sistemlerine yönelik gerçek dünyadaki saldırılarda düşmanlar tarafından kullanılan taktik ve tekniklerin bir bilgi tabanı olan [ATLAS (Yapay-Zeka Sistemleri için Düşmanca Tehdit Manzarası)](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst) oluşturmuştur.

> AI özellikli sistemlerdeki güvenlik açıklarının sayısı artıyor, çünkü AI'nın entegrasyonu mevcut sistemlerin saldırı yüzeyini geleneksel siber saldırıların ötesine genişletiyor. ATLAS'ı bu benzersiz ve gelişen güvenlik açıklarına dikkat çekmek için geliştirdik, çünkü küresel topluluk giderek AI'yı çeşitli sistemlere entegre ediyor. ATLAS, MITRE ATT&CK® çerçevesi üzerine modellenmiştir ve taktik, teknik ve prosedürleri (TTP'ler) ATT&CK'dekilere tamamlayıcıdır.

MITRE ATT&CK® çerçevesine benzer şekilde, geleneksel siber güvenlikte gelişmiş tehdit taklit senaryoları planlamak için yaygın olarak kullanılan ATLAS, yeni ortaya çıkan saldırılara karşı savunma hazırlığı için daha iyi anlamaya yardımcı olabilecek kolayca aranabilir bir TTP seti sağlar.

Ayrıca, Açık Web Uygulama Güvenlik Projesi (OWASP), LLM'leri kullanan uygulamalarda bulunan en kritik güvenlik açıklarının "[En İyi 10 listesi](https://llmtop10.com/?WT.mc_id=academic-105485-koreyst)" oluşturmuştur. Liste, yukarıda bahsedilen veri zehirlenmesi gibi tehditlerin yanı sıra diğerlerini de vurgulamaktadır:

- **Komut Enjeksiyonu**: Saldırganların dikkatle hazırlanmış girdilerle Büyük Dil Modeli'ni (LLM) manipüle ederek, modelin amaçlanan davranışının dışına çıkmasına neden olduğu bir teknik.
- **Tedarik Zinciri Güvenlik Açıkları**: Bir LLM tarafından kullanılan uygulamaları oluşturan bileşenler ve yazılımlar, örneğin Python modülleri veya harici veri kümeleri, kendileri de tehlikeye düşebilir ve beklenmedik sonuçlar, eklenen yanlılıklar ve hatta temel altyapıda güvenlik açıklarına yol açabilir.
- **Aşırı Güven**: LLM'ler hata yapabilir ve yanlış veya güvensiz sonuçlar sağlayabilir. Belgelenmiş birçok durumda, insanlar sonuçları yüzeyde doğru kabul etmiş ve istenmeyen gerçek dünya olumsuz sonuçlarına yol açmıştır.

Microsoft Cloud Advocate Rod Trent, bu ve diğer ortaya çıkan AI tehditlerini derinlemesine inceleyen ve bu senaryoları en iyi şekilde ele almak için kapsamlı rehberlik sağlayan ücretsiz bir ebook, [Must Learn AI Security](https://github.com/rod-trent/OpenAISecurity/tree/main/Must_Learn/Book_Version?WT.mc_id=academic-105485-koreyst) yazmıştır.

## AI Sistemleri ve LLM'ler için Güvenlik Testi

Yapay zeka (AI), çeşitli alanları ve endüstrileri dönüştürerek toplum için yeni olanaklar ve faydalar sunmaktadır. Ancak, AI aynı zamanda veri gizliliği, yanlılık, açıklanabilirlik eksikliği ve potansiyel kötüye kullanım gibi önemli zorluklar ve riskler de taşımaktadır. Bu nedenle, AI sistemlerinin güvenli ve sorumlu olduğundan emin olmak, yani etik ve yasal standartlara uyduğundan ve kullanıcılar ve paydaşlar tarafından güvenilebilir olduğundan emin olmak önemlidir.

Güvenlik testi, bir AI sistemi veya LLM'nin güvenliğini değerlendirerek güvenlik açıklarını belirleme ve kullanma sürecidir. Bu, geliştiriciler, kullanıcılar veya üçüncü taraf denetçiler tarafından, testin amacına ve kapsamına bağlı olarak gerçekleştirilebilir. AI sistemleri ve LLM'ler için en yaygın güvenlik testi yöntemlerinden bazıları şunlardır:

- **Veri temizliği**: Bu, bir AI sistemi veya LLM'nin eğitim verilerinden veya girdisinden hassas veya özel bilgileri kaldırma veya anonimleştirme sürecidir. Veri temizliği, gizli veya kişisel verilerin maruz kalma riskini azaltarak veri sızıntısını ve kötü niyetli manipülasyonu önlemeye yardımcı olabilir.
- **Düşmanca test**: Bu, bir AI sistemi veya LLM'nin girdi veya çıktısına düşmanca örnekler oluşturma ve uygulama sürecidir, böylece sistemin düşmanca saldırılara karşı dayanıklılığını ve direncini değerlendirebilir. Düşmanca test, saldırganlar tarafından istismar edilebilecek AI sistemi veya LLM'nin güvenlik açıklarını ve zayıflıklarını belirlemeye ve hafifletmeye yardımcı olabilir.
- **Model doğrulama**: Bu, bir AI sistemi veya LLM'nin model parametrelerinin veya mimarisinin doğruluğunu ve eksiksizliğini doğrulama sürecidir. Model doğrulama, modelin korunduğunu ve doğrulandığını sağlayarak model hırsızlığını tespit etmeye ve önlemeye yardımcı olabilir.
- **Çıktı doğrulama**: Bu, bir AI sistemi veya LLM'nin çıktısının kalitesini ve güvenilirliğini doğrulama sürecidir. Çıktı doğrulama, çıktının tutarlı ve doğru olduğunu sağlayarak kötü niyetli manipülasyonu tespit etmeye ve düzeltmeye yardımcı olabilir.

OpenAI, AI sistemlerinde lider bir kuruluş olarak, AI güvenliğine katkıda bulunma umuduyla AI sistemlerinin çıktısını test etmeyi amaçlayan kırmızı takım ağ girişimi kapsamında bir dizi _güvenlik değerlendirmesi_ oluşturmuştur.

> Değerlendirmeler, basit Soru-Cevap testlerinden daha karmaşık simülasyonlara kadar çeşitlilik gösterebilir. Somut örnekler olarak, OpenAI tarafından AI davranışlarını çeşitli açılardan değerlendirmek için geliştirilen örnek değerlendirmeler:

#### İkna

- [MakeMeSay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_say/readme.md?WT.mc_id=academic-105485-koreyst): Bir AI sistemi başka bir AI sistemini gizli bir kelime söylemeye ne kadar iyi kandırabilir?
- [MakeMePay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_pay/readme.md?WT.mc_id=academic-105485-koreyst): Bir AI sistemi başka bir AI sistemini para bağışlamaya ne kadar iyi ikna edebilir?
- [Ballot Proposal](https://github.com/openai/evals/tree/main/evals/elsuite/ballots/readme.md?WT.mc_id=academic-105485-koreyst): Bir AI sistemi başka bir AI sisteminin politik bir öneriyi desteklemesini ne kadar iyi etkileyebilir?

#### Steganografi (gizli mesajlaşma)

- [Steganography](https://github.com/openai/evals/tree/main/evals/elsuite/steganography/readme.md?WT.mc_id=academic-105485-koreyst): Bir AI sistemi başka bir AI sistemine yakalanmadan gizli mesajları ne kadar iyi iletebilir?
- [Text Compression](https://github.com/openai/evals/tree/main/evals/elsuite/text_compression/readme.md?WT.mc_id=academic-105485-koreyst): Bir AI sistemi mesajları sıkıştırma ve açma konusunda ne kadar iyi, böylece gizli mesajların gizlenmesini sağlar?
- [Schelling Point](https://github.com/openai/evals/blob/main/evals/elsuite/schelling_point/README.md?WT.mc_id=academic-105485-koreyst): Bir AI sistemi, doğrudan iletişim olmadan başka bir AI sistemiyle ne kadar iyi koordine olabilir?

### AI Güvenliği

AI sistemlerini kötü niyetli saldırılardan, kötüye kullanımdan veya istenmeyen sonuçlardan korumayı amaçlamak zorunludur. Bu, AI sistemlerinin güvenliğini, güvenilirliğini ve güvenilirliğini sağlamak için adımlar atmayı içerir, örneğin:

- AI modellerini eğitmek ve çalıştırmak için kullanılan veri ve algoritmaları güvence altına almak
- AI sistemlerine yetkisiz erişimi, manipülasyonu veya sabotajı önlemek
- AI sistemlerinde yanlılık, ayrımcılık veya etik sorunları tespit etmek ve hafifletmek
- AI kararlarının ve eylemlerinin hesap verebilirliğini, şeffaflığını ve açıklanabilirliğini sağlamak
- AI sistemlerinin hedeflerini ve değerlerini insanlarla ve toplumla uyumlu hale getirmek

AI güvenliği, AI sistemlerinin ve verilerinin bütünlüğünü, kullanılabilirliğini ve gizliliğini sağlamak için önemlidir. AI güvenliğinin bazı zorlukları ve fırsatları şunlardır:

- Fırsat: AI'yı siber güvenlik stratejilerine dahil etmek, çünkü tehditleri tanımlamada ve yanıt sürelerini iyileştirmede kritik bir rol oynayabilir. AI, kimlik avı, kötü amaçlı yazılım veya fidye yazılımı gibi siber saldırıların algılanmasını ve hafifletilmesini otomatikleştirmeye ve artırmaya yardımcı olabilir.
- Zorluk: AI, düşmanlar tarafından sahte veya yanıltıcı içerik oluşturma, kullanıcıları taklit etme veya AI sistemlerindeki güvenlik açıklarını istismar etme gibi sofistike saldırılar başlatmak için kullanılabilir. Bu nedenle, AI geliştiricileri, kötüye kullanıma karşı dayanıklı ve sağlam sistemler tasarlama konusunda özel bir sorumluluğa sahiptir.

### Veri Koruma

LLM'ler, kullandıkları verilerin gizliliği ve güvenliği açısından riskler taşıyabilir. Örneğin, LLM'ler, eğitim verilerinden kişisel adlar, adresler, şifreler veya kredi kartı numaraları gibi hassas bilgileri ezberleyebilir ve sızdırabilir. Ayrıca, kötü niyetli aktörler tarafından istismar edilmek veya yanlılıkları istismar edilmek için manipüle edilebilir veya saldırıya uğrayabilirler. Bu nedenle, bu risklerin farkında olmak ve LLM'lerle kullanılan verileri korumak için uygun önlemleri almak önemlidir. LLM'lerle kullanılan verileri korumak için atabileceğiniz birkaç adım vardır. Bu adımlar şunları içerir:

- **LLM'lerle paylaşılan veri miktarını ve türünü sınırlamak**: Yalnızca amaçlanan amaçlar için gerekli ve ilgili verileri paylaşın ve hassas, gizli veya kişisel verileri paylaşmaktan kaçının. Kullanıcılar ayrıca LLM'lerle paylaştıkları verileri anonimleştirmeli veya şifrelemelidir, örneğin herhangi bir tanımlayıcı bilgiyi kaldırarak veya maskeleyerek veya güvenli iletişim kanalları kullanarak.
- **LLM'lerin ürettiği verileri doğrulamak**: LLM'ler tarafından üretilen çıktının doğruluğunu ve kalitesini kontrol edin, böylece istenmeyen veya uygunsuz bilgiler içermediğinden emin olun.
- **Herhangi bir veri ihlalini veya olayını bildirme ve uyarma**: LLM'lerden gelen herhangi bir şüpheli veya anormal etkinlik veya davranışa karşı dikkatli olun, örneğin alakasız, yanlış, saldırgan veya zararlı metinler üretmek. Bu, bir veri ihlali veya güvenlik olayının göstergesi olabilir.

Veri güvenliği, yönetimi ve uyumu, çoklu bulut ortamında veri ve AI'nın gücünden yararlanmak isteyen herhangi bir kuruluş için kritik öneme sahiptir. Tüm verilerinizi güvence altına almak ve yönetmek karmaşık ve çok yönlü bir çabadır. Farklı bulutlar arasında farklı konumlarda farklı türde verileri (yapılandırılmış, yapılandırılmamış ve AI tarafından üretilen veriler) güvence altına almanız ve yönetmeniz ve mevcut ve gelecekteki veri güvenliği, yönetimi ve AI düzenlemelerini dikkate almanız gerekir. Verilerinizi korumak için en iyi uygulamaları ve önlemleri benimsemelisiniz, örneğin:

- Veri koruma ve gizlilik özellikleri sunan bulut hizmetlerini veya platformlarını kullanın.
- Verilerinizi hatalar, tutarsızlıklar veya anomaliler açısından kontrol etmek için veri kalitesi ve doğrulama araçlarını kullanın.
- Verilerinizin sorumlu ve şeffaf bir şekilde kullanılmasını sağlamak için veri yönetimi ve etik çerçevelerini kullanın.

### Gerçek dünya tehditlerini taklit etme - AI kırmızı takım çalışması

Gerçek dünya tehditlerini taklit etmek, sistemlere yönelik riskleri belirlemek ve savunucuların tepkisini test etmek için benzer araçlar, taktikler ve prosedürler kullanarak dayanıklı AI sistemleri oluşturmakta artık standart bir uygulama olarak kabul edilmektedir.

> AI kırmızı takım çalışması uygulaması, daha geniş bir anlam kazanmaya evrildi: yalnızca güvenlik açıklarını araştırmayı kapsamakla kalmaz, aynı zamanda potansiyel olarak zararlı içerik üretimi gibi diğer sistem hatalarını araştırmayı da içerir. AI sistemleri yeni risklerle gelir ve kırmızı takım çalışması, bu yeni riskleri anlamanın merkezinde yer alır, örneğin komut enjeksiyonu ve temelsiz içerik üretimi. - [Microsoft AI Red Team daha güvenli AI'nın gelece

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluğu sağlamak için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belgenin kendi dilindeki hali, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından doğabilecek yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.