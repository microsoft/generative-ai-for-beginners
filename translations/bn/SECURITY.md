<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2d33a71bed73d6daee78e2d473ece975",
  "translation_date": "2025-07-09T06:52:17+00:00",
  "source_file": "SECURITY.md",
  "language_code": "bn"
}
-->
## সুরক্ষা

Microsoft আমাদের সফটওয়্যার পণ্য এবং পরিষেবাগুলোর সুরক্ষা গুরুত্বের সাথে গ্রহণ করে, যার মধ্যে রয়েছে আমাদের GitHub সংস্থাগুলোর মাধ্যমে পরিচালিত সমস্ত সোর্স কোড রিপোজিটরি, যেমন [Microsoft](https://github.com/microsoft), [Azure](https://github.com/Azure), [DotNet](https://github.com/dotnet), [AspNet](https://github.com/aspnet), [Xamarin](https://github.com/xamarin), এবং [আমাদের GitHub সংস্থাগুলো](https://opensource.microsoft.com/)।

আপনি যদি মনে করেন যে Microsoft-সম্পত্তি কোনো রিপোজিটরিতে এমন একটি সুরক্ষা দুর্বলতা খুঁজে পেয়েছেন যা [Microsoft-এর সুরক্ষা দুর্বলতার সংজ্ঞা](https://aka.ms/opensource/security/definition) পূরণ করে, তাহলে অনুগ্রহ করে নিচে বর্ণিত পদ্ধতিতে আমাদের জানাবেন।

## সুরক্ষা সমস্যা রিপোর্ট করা

**দয়া করে পাবলিক GitHub ইস্যুর মাধ্যমে সুরক্ষা দুর্বলতা রিপোর্ট করবেন না।**

তার পরিবর্তে, অনুগ্রহ করে Microsoft Security Response Center (MSRC)-এ রিপোর্ট করুন [https://msrc.microsoft.com/create-report](https://aka.ms/opensource/security/create-report) এ।

আপনি যদি লগইন না করে জমা দিতে চান, তাহলে ইমেইল পাঠান [secure@microsoft.com](mailto:secure@microsoft.com) এ। সম্ভব হলে, আমাদের PGP কী দিয়ে আপনার বার্তাটি এনক্রিপ্ট করুন; এটি ডাউনলোড করতে পারেন [Microsoft Security Response Center PGP Key পেজ থেকে](https://aka.ms/opensource/security/pgpkey)।

আপনি ২৪ ঘণ্টার মধ্যে একটি প্রতিক্রিয়া পাবেন। যদি কোনো কারণে না পান, তাহলে নিশ্চিত করার জন্য ইমেইলের মাধ্যমে ফলোআপ করুন যাতে আমরা আপনার মূল বার্তাটি পেয়েছি। অতিরিক্ত তথ্য পাওয়া যাবে [microsoft.com/msrc](https://aka.ms/opensource/security/msrc) এ।

অনুগ্রহ করে নিচের অনুরোধকৃত তথ্যগুলো (যতটা সম্ভব দিতে পারেন) অন্তর্ভুক্ত করুন যাতে আমরা সম্ভাব্য সমস্যার প্রকৃতি এবং পরিধি ভালোভাবে বুঝতে পারি:

  * সমস্যার ধরন (যেমন buffer overflow, SQL injection, cross-site scripting ইত্যাদি)
  * সমস্যার প্রকাশ ঘটানো সোর্স ফাইল(গুলি)র সম্পূর্ণ পথ
  * প্রভাবিত সোর্স কোডের অবস্থান (tag/branch/commit বা সরাসরি URL)
  * সমস্যা পুনরুত্পাদনের জন্য প্রয়োজনীয় বিশেষ কনফিগারেশন
  * সমস্যা পুনরুত্পাদনের ধাপে ধাপে নির্দেশনা
  * প্রুফ-অফ-কনসেপ্ট বা exploit কোড (যদি সম্ভব হয়)
  * সমস্যার প্রভাব, এবং কীভাবে একজন আক্রমণকারী এটি কাজে লাগাতে পারে

এই তথ্যগুলো আমাদের রিপোর্ট দ্রুত প্রক্রিয়াকরণে সাহায্য করবে।

আপনি যদি বাগ বাউন্টির জন্য রিপোর্ট করছেন, তাহলে আরও সম্পূর্ণ রিপোর্ট উচ্চতর বাউন্টি পুরস্কারে অবদান রাখতে পারে। আমাদের [Microsoft Bug Bounty Program](https://aka.ms/opensource/security/bounty) পেজে আমাদের সক্রিয় প্রোগ্রামগুলোর বিস্তারিত তথ্য পাওয়া যাবে।

## পছন্দসই ভাষা

আমরা সব যোগাযোগ ইংরেজিতে হওয়াকে অগ্রাধিকার দিই।

## নীতি

Microsoft [Coordinated Vulnerability Disclosure](https://aka.ms/opensource/security/cvd) নীতিমালা অনুসরণ করে।

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।