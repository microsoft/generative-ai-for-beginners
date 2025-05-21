<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f3cac698e9eea47dd563633bd82daf8c",
  "translation_date": "2025-05-19T22:44:21+00:00",
  "source_file": "13-securing-ai-applications/README.md",
  "language_code": "tr"
}
-->
# Üretken AI Uygulamalarınızı Güvenceye Alma

## Giriş

Bu derste şunlar ele alınacaktır:

- AI sistemleri bağlamında güvenlik.
- AI sistemlerine yönelik yaygın riskler ve tehditler.
- AI sistemlerini güvence altına alma yöntemleri ve dikkate alınması gerekenler.

## Öğrenme Hedefleri

Bu dersi tamamladıktan sonra, şunları anlayabileceksiniz:

- AI sistemlerine yönelik tehditler ve riskler.
- AI sistemlerini güvence altına almak için yaygın yöntemler ve uygulamalar.
- Güvenlik testlerinin uygulanmasının beklenmedik sonuçları ve kullanıcı güveninin aşınmasını nasıl önleyebileceği.

## Üretken AI bağlamında güvenlik ne anlama gelir?

Yapay Zeka (AI) ve Makine Öğrenimi (ML) teknolojileri hayatımızı giderek daha fazla şekillendirdikçe, yalnızca müşteri verilerini değil, aynı zamanda AI sistemlerini de korumak hayati önem taşır. AI/ML, yanlış kararların ciddi sonuçlara yol açabileceği sektörlerde yüksek değerli karar verme süreçlerini desteklemek için giderek daha fazla kullanılmaktadır.

Dikkate alınması gereken önemli noktalar şunlardır:

- **AI/ML'nin Etkisi**: AI/ML günlük yaşam üzerinde önemli etkilere sahiptir ve bu nedenle onları korumak zorunlu hale gelmiştir.
- **Güvenlik Zorlukları**: AI/ML'nin bu etkisi, ister troller ister organize gruplar tarafından olsun, AI tabanlı ürünleri sofistike saldırılardan koruma ihtiyacını ele almak için uygun dikkat gerektirir.
- **Stratejik Sorunlar**: Teknoloji endüstrisi, uzun vadeli müşteri güvenliğini ve veri güvenliğini sağlamak için stratejik zorlukları proaktif bir şekilde ele almalıdır.

Ayrıca, Makine Öğrenimi modelleri, kötü niyetli girdi ile zararsız anormal verileri ayırt edemez. Eğitim verilerinin önemli bir kaynağı, üçüncü taraf katkılarına açık, düzenlenmemiş, denetlenmemiş, kamuya açık veri kümelerinden türetilir. Saldırganların veri kümelerini ele geçirmesi gerekmez, çünkü katkıda bulunmakta serbesttirler. Zamanla, düşük güvenilirlikteki kötü niyetli veriler, veri yapısı/formatı doğru kaldığı sürece yüksek güvenilirlikte güvenilir verilere dönüşür.

Bu nedenle, modellerinizin karar vermek için kullandığı veri depolarının bütünlüğünü ve korunmasını sağlamak kritik öneme sahiptir.

## AI'nin tehditlerini ve risklerini anlama

AI ve ilgili sistemler açısından, veri zehirlenmesi bugün en önemli güvenlik tehdidi olarak öne çıkmaktadır. Veri zehirlenmesi, birinin AI'yi eğitmek için kullanılan bilgileri kasıtlı olarak değiştirerek hatalar yapmasına neden olduğu durumdur. Bu, standart tespit ve hafifletme yöntemlerinin eksikliği ve eğitim için güvenilmeyen veya düzenlenmemiş kamuya açık veri kümelerine olan bağımlılığımız nedeniyle ortaya çıkmaktadır. Veri bütünlüğünü sağlamak ve hatalı bir eğitim sürecini önlemek için verilerinizin kaynağını ve soyunu izlemek önemlidir. Aksi takdirde, "çöp girerse, çöp çıkar" sözü geçerli olur ve model performansı tehlikeye girer.

Veri zehirlenmesinin modellerinizi nasıl etkileyebileceğine dair örnekler:

1. **Etiket Değiştirme**: İkili sınıflandırma görevinde, bir saldırgan eğitim verilerinin küçük bir alt kümesinin etiketlerini kasıtlı olarak değiştirir. Örneğin, zararsız örnekler kötü niyetli olarak etiketlenir ve model yanlış ilişkiler öğrenir.\
   **Örnek**: Etiketleri değiştirilmiş spam filtresi nedeniyle yasal e-postaları spam olarak yanlış sınıflandırmak.
2. **Özellik Zehirlenmesi**: Bir saldırgan, modelin yanlı veya yanıltıcı hale gelmesi için eğitim verilerindeki özellikleri kurnazca değiştirir.\
   **Örnek**: Ürün açıklamalarına alakasız anahtar kelimeler ekleyerek öneri sistemlerini manipüle etmek.
3. **Veri Enjeksiyonu**: Modelin davranışını etkilemek için eğitim setine kötü niyetli veri enjekte etmek.\
   **Örnek**: Sahte kullanıcı yorumları ekleyerek duygu analiz sonuçlarını çarpıtmak.
4. **Arka Kapı Saldırıları**: Bir saldırgan, eğitim verilerine gizli bir desen (arka kapı) ekler. Model bu deseni tanımayı öğrenir ve tetiklendiğinde kötü niyetli davranır.\
   **Örnek**: Arka kapılı görüntülerle eğitilmiş bir yüz tanıma sistemi, belirli bir kişiyi yanlış tanımlar.

MITRE Corporation, AI sistemlerine yönelik gerçek dünya saldırılarında düşmanlar tarafından kullanılan taktik ve tekniklerin bir bilgi tabanı olan [ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems)](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst) oluşturdu.

> AI özellikli sistemlerdeki güvenlik açıklarının sayısı artıyor, çünkü AI'nin entegrasyonu, mevcut sistemlerin saldırı yüzeyini geleneksel siber saldırıların ötesine taşıyor. ATLAS'ı, küresel topluluk çeşitli sistemlere AI'yi giderek daha fazla entegre ettikçe, bu benzersiz ve gelişen güvenlik açıkları konusunda farkındalık yaratmak için geliştirdik. ATLAS, MITRE ATT&CK® çerçevesini temel alır ve taktik, teknik ve prosedürleri (TTP'ler) ATT&CK'dekilere tamamlayıcıdır.

Geleneksel siber güvenlikte ileri tehdit emülasyon senaryolarını planlamak için yaygın olarak kullanılan MITRE ATT&CK® çerçevesine benzer şekilde, ATLAS, ortaya çıkan saldırılara karşı savunmayı daha iyi anlamaya ve hazırlanmaya yardımcı olabilecek kolayca aranabilir bir TTP seti sunar.

Ayrıca, Open Web Application Security Project (OWASP), LLM'leri kullanan uygulamalarda bulunan en kritik güvenlik açıklarının bir "[En İyi 10 listesi](https://llmtop10.com/?WT.mc_id=academic-105485-koreyst)" oluşturdu. Liste, yukarıda bahsedilen veri zehirlenmesi gibi tehditlerin yanı sıra diğer riskleri de vurgular:

- **Prompt Enjeksiyonu**: Saldırganların dikkatlice hazırlanmış girdilerle Büyük Dil Modeli'ni (LLM) manipüle ederek, modelin beklenmedik davranmasına neden olduğu bir teknik.
- **Tedarik Zinciri Güvenlik Açıkları**: Bir LLM tarafından kullanılan uygulamaları oluşturan bileşenler ve yazılımlar, Python modülleri veya harici veri setleri gibi, beklenmedik sonuçlara, tanıtılan önyargılara ve hatta temel altyapıda güvenlik açıklarına yol açarak kendileri tehlikeye atılabilir.
- **Aşırı Güven**: LLM'ler yanılgıya düşebilir ve yanlış veya güvensiz sonuçlar sağlayabilir. Birçok belgelenmiş durumda, insanlar sonuçları olduğu gibi kabul etmiş ve istenmeyen gerçek dünya olumsuz sonuçlarına yol açmıştır.

Microsoft Cloud Advocate Rod Trent, bu ve diğer ortaya çıkan AI tehditlerine derinlemesine dalan ve bu senaryoları en iyi şekilde ele almak için kapsamlı rehberlik sağlayan ücretsiz bir e-kitap, [Must Learn AI Security](https://github.com/rod-trent/OpenAISecurity/tree/main/Must_Learn/Book_Version?WT.mc_id=academic-105485-koreyst) yazmıştır.

## AI Sistemleri ve LLM'ler için Güvenlik Testi

Yapay zeka (AI), çeşitli alanları ve endüstrileri dönüştürerek toplum için yeni olanaklar ve faydalar sunmaktadır. Ancak, AI aynı zamanda veri gizliliği, önyargı, açıklanabilirlik eksikliği ve potansiyel kötüye kullanım gibi önemli zorluklar ve riskler de taşır. Bu nedenle, AI sistemlerinin güvenli ve sorumlu olduğundan emin olmak hayati önem taşır; bu, etik ve yasal standartlara uygun oldukları ve kullanıcılar ve paydaşlar tarafından güvenilebilir oldukları anlamına gelir.

Güvenlik testi, bir AI sistemi veya LLM'nin güvenliğini değerlendirme sürecidir ve bu süreç, güvenlik açıklarını belirleyip istismar etmeyi içerir. Bu, testin amacına ve kapsamına bağlı olarak geliştiriciler, kullanıcılar veya üçüncü taraf denetçiler tarafından gerçekleştirilebilir. AI sistemleri ve LLM'ler için en yaygın güvenlik test yöntemlerinden bazıları şunlardır:

- **Veri temizleme**: Bu, bir AI sistemi veya LLM'nin eğitim verilerinden veya girdilerinden hassas veya özel bilgileri kaldırma veya anonimleştirme sürecidir. Veri temizleme, gizli veya kişisel verilerin maruz kalmasını azaltarak veri sızıntısını ve kötü niyetli manipülasyonu önlemeye yardımcı olabilir.
- **Düşman testi**: Bu, bir AI sistemi veya LLM'nin girdi veya çıktısına düşman örnekler oluşturarak ve uygulayarak, sistemin düşman saldırılarına karşı dayanıklılığını ve direncini değerlendirme sürecidir. Düşman testi, saldırganlar tarafından istismar edilebilecek bir AI sistemi veya LLM'nin zayıf noktalarını ve güvenlik açıklarını belirlemeye ve hafifletmeye yardımcı olabilir.
- **Model doğrulama**: Bu, bir AI sistemi veya LLM'nin model parametrelerinin veya mimarisinin doğruluğunu ve bütünlüğünü doğrulama sürecidir. Model doğrulama, modelin korunduğunu ve doğrulandığını sağlayarak model çalınmasını tespit etmeye ve önlemeye yardımcı olabilir.
- **Çıktı doğrulama**: Bu, bir AI sistemi veya LLM'nin çıktısının kalitesini ve güvenilirliğini doğrulama sürecidir. Çıktı doğrulama, çıktının tutarlı ve doğru olduğundan emin olarak kötü niyetli manipülasyonu tespit etmeye ve düzeltmeye yardımcı olabilir.

AI sistemlerinde lider olan OpenAI, AI güvenliğine katkıda bulunma umuduyla, kırmızı takım ağı girişimi kapsamında AI sistemlerinin çıktısını test etmeye yönelik bir dizi _güvenlik değerlendirmesi_ kurmuştur.

> Değerlendirmeler, basit Soru-Cevap testlerinden daha karmaşık simülasyonlara kadar değişebilir. İşte, OpenAI tarafından AI davranışlarını çeşitli açılardan değerlendirmek için geliştirilen örnek değerlendirmeler:

#### İkna

- [MakeMeSay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_say/readme.md?WT.mc_id=academic-105485-koreyst): Bir AI sistemi başka bir AI sistemini gizli bir kelime söylemeye ne kadar iyi kandırabilir?
- [MakeMePay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_pay/readme.md?WT.mc_id=academic-105485-koreyst): Bir AI sistemi başka bir AI sistemini para bağışlamaya ne kadar iyi ikna edebilir?
- [Ballot Proposal](https://github.com/openai/evals/tree/main/evals/elsuite/ballots/readme.md?WT.mc_id=academic-105485-koreyst): Bir AI sistemi başka bir AI sisteminin siyasi bir öneriyi desteklemesini ne kadar iyi etkileyebilir?

#### Steganografi (gizli mesajlaşma)

- [Steganography](https://github.com/openai/evals/tree/main/evals/elsuite/steganography/readme.md?WT.mc_id=academic-105485-koreyst): Bir AI sistemi başka bir AI sistemi tarafından yakalanmadan gizli mesajları ne kadar iyi iletebilir?
- [Text Compression](https://github.com/openai/evals/tree/main/evals/elsuite/text_compression/readme.md?WT.mc_id=academic-105485-koreyst): Bir AI sistemi mesajları sıkıştırma ve açma konusunda ne kadar iyi, gizli mesajları saklamayı sağlamak için?
- [Schelling Point](https://github.com/openai/evals/blob/main/evals/elsuite/schelling_point/README.md?WT.mc_id=academic-105485-koreyst): Bir AI sistemi, doğrudan iletişim olmadan başka bir AI sistemiyle ne kadar iyi koordine olabilir?

### AI Güvenliği

AI sistemlerini kötü niyetli saldırılardan, kötüye kullanımdan veya istenmeyen sonuçlardan korumayı hedeflemek zorunludur. Bu, AI sistemlerinin güvenliğini, güvenilirliğini ve güvenilirliğini sağlamak için adımlar atmayı içerir, örneğin:

- AI modellerini eğitmek ve çalıştırmak için kullanılan veri ve algoritmaları güvence altına almak
- AI sistemlerine yetkisiz erişimi, manipülasyonu veya sabotajını önlemek
- AI sistemlerindeki önyargı, ayrımcılık veya etik sorunları tespit etmek ve hafifletmek
- AI kararlarının ve eylemlerinin hesap verebilirliğini, şeffaflığını ve açıklanabilirliğini sağlamak
- AI sistemlerinin hedeflerini ve değerlerini insan ve toplumunkilerle uyumlu hale getirmek

AI güvenliği, AI sistemlerinin ve verilerin bütünlüğünü, kullanılabilirliğini ve gizliliğini sağlamak için önemlidir. AI güvenliğinin bazı zorlukları ve fırsatları şunlardır:

- Fırsat: AI'yi siber güvenlik stratejilerine entegre etmek, tehditleri tanımlamada ve yanıt sürelerini iyileştirmede önemli bir rol oynayabilir. AI, kimlik avı, kötü amaçlı yazılım veya fidye yazılımı gibi siber saldırıların tespit ve hafifletilmesini otomatikleştirmeye ve artırmaya yardımcı olabilir.
- Zorluk: AI, düşmanlar tarafından sahte veya yanıltıcı içerik üretme, kullanıcıları taklit etme veya AI sistemlerindeki güvenlik açıklarını istismar etme gibi sofistike saldırılar başlatmak için de kullanılabilir. Bu nedenle, AI geliştiricilerinin kötüye kullanıma karşı dayanıklı ve sağlam sistemler tasarlama konusunda özel bir sorumluluğu vardır.

### Veri Koruma

LLM'ler, kullandıkları verilerin gizliliği ve güvenliği açısından riskler oluşturabilir. Örneğin, LLM'ler, eğitim verilerinden kişisel isimler, adresler, şifreler veya kredi kartı numaraları gibi hassas bilgileri ezberleyebilir ve sızdırabilir. Ayrıca, kötü niyetli aktörler tarafından güvenlik açıklarını veya önyargılarını istismar etmek isteyenler tarafından manipüle edilebilir veya saldırıya uğrayabilirler. Bu nedenle, bu risklerin farkında olmak ve LLM'lerle kullanılan verileri korumak için uygun önlemleri almak önemlidir. LLM'lerle kullanılan verileri korumak için atabileceğiniz birkaç adım vardır. Bu adımlar şunları içerir:

- **LLM'lerle paylaşılan veri miktarını ve türünü sınırlamak**: Yalnızca gerekli ve ilgili verileri paylaşın ve hassas, gizli veya kişisel verileri paylaşmaktan kaçının. Kullanıcılar ayrıca LLM'lerle paylaştıkları verileri anonimleştirmeli veya şifrelemelidir, örneğin herhangi bir tanımlayıcı bilgiyi kaldırarak veya maskeleyerek ya da güvenli iletişim kanalları kullanarak.
- **LLM'lerin ürettiği verileri doğrulamak**: LLM'ler tarafından üretilen çıktının istenmeyen veya uygunsuz bilgi içermediğinden emin olmak için her zaman doğruluğunu ve kalitesini kontrol edin.
- **Herhangi bir veri ihlali veya olayı bildirme ve uyarma**: LLM'lerden gelen alakasız, yanlış, saldırgan veya zararlı metinler gibi şüpheli veya anormal etkinliklere veya davranışlara karşı dikkatli olun. Bu, bir veri ihlali veya güvenlik olayı belirtisi olabilir.

Veri güvenliği, yönetimi ve uyumluluğu, çoklu bulut ortamında veri ve AI'nin gücünden yararlanmak isteyen herhangi bir kuruluş için kritik öneme sahiptir. Tüm verilerinizi güvence altına almak ve yönetmek karmaşık ve çok yönlü bir iştir. Farklı bulutlar arasında farklı konumlarda farklı türdeki verileri (yapılandırılmış, yapılandırılmamış ve AI tarafından üretilen veriler) güvence altına almanız ve yönetmeniz ve mevcut ve gelecekteki veri güvenliği, yönetimi ve AI düzenlemelerini hesaba katmanız gerekir. Verilerinizi korumak için bazı en iyi uygulamaları ve önlemleri benimsemeniz gerekir, örneğin:

- Veri koruma ve gizlilik özellikleri sunan bulut hizmetlerini veya platformlarını kullanın.
- Verilerinizi hatalar, tutarsızlıklar veya anormallikler için kontrol etmek için veri kalitesi ve doğrulama araçlarını kullanın.
- Verilerinizin sorumlu ve şeffaf bir şekilde kullanıldığından emin olmak için veri yönetimi ve etik çerçeveleri kullanın.

### Gerçek dünya tehditlerini taklit etme - AI kırmızı takım çalışması

Gerçek dünya tehditlerini taklit etmek, sistemlerin risklerini belirlemek ve savunucuların tepkisini test etmek için benzer araçlar, taktikler, prosedürler kullanarak dayanıklı AI sistemleri inşa etmede artık standart bir uygulama olarak kabul edilmektedir.

> AI kırmızı takım çalışması uygulaması, daha geniş bir anlam kazanacak şekilde evrimleşti: yalnızca güvenlik açıklarını araştırmayı değil, aynı zamanda potansiyel olarak zararlı içerik üretimi gibi diğer sistem hatalarını da araştırmayı kapsar. AI sistemleri yeni riskler taşır ve kırmızı takım çalışması, bu yeni riskleri anlamanın merkezindedir, örneğin prompt enjeksiyonu ve temelsiz içerik üretimi. - [Microsoft AI Red Team daha güvenli AI'nin geleceğini inşa ediyor](https://www.microsoft.com/security/blog/2023/08

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini unutmayın. Belgenin orijinal dilindeki hali yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.