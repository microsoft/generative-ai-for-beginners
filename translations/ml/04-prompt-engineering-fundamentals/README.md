# പ്രോംപ്‌റ്റ് എഞ്ചിനീയറിംഗ് അടിസ്ഥാനങ്ങളും

[![പ്രോംപ്‌റ്റ് എഞ്ചിനീയറിംഗ് അടിസ്ഥാനങ്ങൾ](../../../translated_images/ml/04-lesson-banner.a2c90deba7fedacd.webp)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## പരിചയം  
ഈ മോഡ്യൂള്‍ ജനറേറ്റീവ് എ.ഐ. മോഡലുകളിലെ ഫലപ്രദമായ പ്രോംപ്‌ടുകൾ സൃഷ്ടിക്കുന്നതിനുള്ള അടിസ്ഥാന ആശയങ്ങളും സാങ്കേതിക വിദ്യകളും ഉള്‍ക്കൊള്ളുന്നു. ഒരു LLM-ന് നിങ്ങൾ എഴുതുന്ന പ്രോംപ്‌റ്റ് എങ്ങനെ ആയിരിക്കണമെന്ന് കൂടി പരിഗണിക്കണം. സൂക്ഷ്മമായി രൂപകല്‍പ്പന ചെയ്ത ഒരു പ്രോംപ്‌ട് മികച്ച നിലവാരത്തിലുള്ള പ്രതികരണം നേടാന്‍ സഹായിക്കും. പക്ഷെ _പ്രോംപ്‌റ്_ എന്ന പദം ഉം _പ്രോംപ്‌റ്റ് എഞ്ചിനീയറിംഗ്_ എന്നത് എന്താണ് അർത്ഥമാക്കുന്നത്? LLM-ന് അയക്കുന്ന പ്രോംപ്‌റ് _ഇൻപുട്ട്_ എങ്ങനെ മെച്ചപ്പെടുത്താം? ഈ ചോദ്യങ്ങൾക്ക് ഈ അധ്യായത്തിലും അടുത്തവന്നും ഞങ്ങൾ ഉത്തരങ്ങൾ തേടും.

_ജനനക്ഷമമായ എ.ഐ._ ഉപയോക്തൃ അഭ്യര്‍ത്ഥനകളെ ഉത്തരം പറയുന്നതിന് പുതിയ ഉള്ളടക്കം (ഉദാ: എഴുത്ത്, ചിത്രങ്ങൾ, ഓഡിയോ, കോഡ് എന്നിവ) സൃഷ്ടിക്കാൻ കഴിയും. ഇത് OpenAI-യുടെ GPT ("ജനറേറ്റീവ് പ്രീ-ട്രേഡ് ട്രാൻസ്ഫോർമർ") സീരീസ് പോലുള്ള _വലിയ ഭാഷാ മോഡലുകൾ_ ഉപയോഗിച്ച് സമ്പ്രദായിക ഭാഷയും കോഡും ഉപയോഗിച്ച് പരിശീലനം നേടിയാണ് സാധ്യമാക്കുന്നത്.

ഉപയോക്താക്കൾക്ക് ഇനി تکنیکی പരിശീലനം ആവശ്യമില്ലാതെ ചാറ്റ് പോലുള്ള പരിചിതമായ മാതൃകകളിലൂടെ ഈ മോഡലുകളുമായി ഇടപഴകാൻ കഴിയും. മോഡലുകൾ _പ്രോംപ്‌റ്റ് അടിസ്ഥാനമാക്കിയതാണ്_ - ഉപയോഗക്കാർ ഒരു ടെക്സ്റ്റ് ഇൻപുട്ട് (പ്രോംപ്‌ട്) അയച്ച് എ.ഐ. പ്രതികരണം (കമ്പ്ലീഷന്‍) ലഭിക്കുന്നു. പിന്നെ അവര്‍ പുനരാവൃത്തിയായി പ്രോംപ്‌റ്റുകളിലൂടെ "എ.ഐ. എന്നോരു ചാറ്റിൽ" സംഭാഷണം നടത്തുകയും, പ്രതീക്ഷിക്കുന്ന ഉത്തരം ലഭിക്കുന്നതുവരെ പ്രോംപ്‌ട് മെച്ചപ്പെടുത്തുകയും ചെയ്യാം.

"പ്രോംപ്‌റുകൾ" ഇപ്പോൾ ജനറേറ്റീവ് എ.ഐ. ആപ്പുകൾക്കുള്ള പ്രധാന _പ്രോഗ്രാമിങ് ഇന്റർഫേസ്_ ആയി മാറിയിരിക്കുന്നു, മോഡലുകളെ എന്ത് ചെയ്യണമെന്നു പറയുകയും തിരികുള്ള പ്രതികരണങ്ങളുടെ ഗുണമേന്മയെ സ്വാധീനിക്കുകയും ചെയ്യുന്നു. "പ്രോംപ്‌റ്റ് എഞ്ചിനീയറിംഗ്" ഒരു വേഗത്തിൽ വളരുന്ന പഠന മേഖലയാണ്, സ്ഥിരതയുള്ളയും ഗുണമേന്മയുള്ളവുമായ പ്രതികരണങ്ങൾ വലുതായി ലഭ്യമാകാൻ പ്രോംപ്‌റുകളുടെ _ഡിസൈൻവും ഓപ്റ്റിമൈസേഷനും_ കുറിച്ച് ശ്രദ്ധ ചെലുത്തുന്നു.

## പഠന ലക്ഷ്യങ്ങൾ

ഈ പാഠത്തിൽ, പ്രോംപ്‌റ്റ് എഞ്ചിനീയറിംഗ് എന്താണ്, അതിനിപ്പോഴേ എന്തുകൊണ്ടാണ് ഇത് ബാധകമാകുന്നത്, ഒരു പ്രഖ്യാപിത മോഡലിനും ആപ്ലിക്കേഷൻ ലക്ഷ്യത്തിനും അനുയോജ്യമായ പ്രകാരം ഫലപ്രദമായ പ്രോംപ്‌റുകൾ എങ്ങനെ രൂപകല്‍പ്പന ചെയ്യാമെന്ന് നാം പഠിക്കും. പ്രോംപ്‌റ്റ് എഞ്ചിനീയറിംഗിൻറെ മുഖ്യ ആശയങ്ങളും മികച്ച പ്രയോഗരീതികളും മനസ്സിലാക്കുകയും ജ്യൂപിറ്റർ നോട്ട്ബുക്കുകൾ ഉപയോഗിച്ച് കാര്യക്ഷമ സാമ്പിൾ സംവരണങ്ങള്‍ കാണുകയും ചെയ്യും.

ഈ പാഠത്തിന്റെ അവസാനം നാം സാധിക്കുമെന്ന്:

1. പ്രോംപ്‌റ്റ് എഞ്ചിനീയറിംഗ്‌ എന്താണെന്ന് വിശദീകരിക്കാം, അതിനൊക്കെ പ്രാധാന്യം എന്താണെന്ന് മനസ്സിലാക്കാം.
2. ഒരു പ്രോംപ്‌റ്റിലെ ഘടകങ്ങൾ എന്തൊക്കെയാണെന്ന് വിശദീകരിക്കാം, അവ എങ്ങനെ ഉപയോഗിക്കപ്പെടുന്നു.
3. പ്രോംപ്‌റ്റ് എഞ്ചിനീയറിംഗിനുള്ള മികച്ച രീതികളും സാങ്കേതിക വിദ്യകളും പഠിക്കാം.
4. പഠിച്ച സാങ്കേതിക വിദ്യകൾ യാഥാർത്ഥ്യ ഉദാഹരണങ്ങളിൽ OpenAI എൻഡ്പോയിന്റ് ഉപയോഗിച്ച് പ്രയോഗിക്കാം.

## പ്രധാന പദങ്ങൾ

പ്രോംപ്‌റ്റ് എഞ്ചിനീയറിംഗ്: ആവശ്യമായ ഔട്ട്പുട്ടുകൾ ലഭിക്കാനായി എ.ഐ. മോഡലുകളെ നയിക്കുന്നതിന് ഇൻപുട്ടുകളെ രൂപകൽപ്പന ചെയ്യുകയും മെച്ചപ്പെടുത്തുകയും 하는 പ്രക്രിയ.  
ടോകനൈസേഷൻ: ഒരു മോഡൽ മനസിലാക്കുകയും പ്രോസസ്സ് ചെയ്യുകയും ചെയ്യാൻ കഴിയുന്ന ചെറിയ ഘടകങ്ങളായ ടോകണുകളായി ടെക്സ്റ്റ് മാറ്റാനുള്ള പ്രക്രിയ.  
ഇൻസ്റ്റ്രക്ഷൻ-ട്യൂൺ ചെയ്ത LLMകൾ: പ്രത്യേക നിർദ്ദേശങ്ങൾ ഉപയോഗിച്ചുകൊണ്ട് പ്രതികരണത്തിന്റെ കൃത്യതയും പ്രസക്തിയുമെച്ചപ്പെടുത്താൻ ഫൈൻ-ട്യൂൺ ചെയ്ത വലിയ ഭാഷാ മോഡലുകൾ.

## പഠന സാമ്പ്‌ബോക്സ്

പ്രോംപ്‌റ്റ് എഞ്ചിനീയറിംഗ് ഇപ്പോൾ ശാസ്ത്രത്തിലേക്കുള്ള കലയാണെന്ന് പറയാം. അതിൽ വല്ലാതെ സമ്മർദ്ദം നല്‍കുന്ന വിധം അറിവ് മെച്ചപ്പെടുത്താൻ നല്ല മാർഗ്ഗം _കൂടുതൽ പ്രാക്ടീസ്_ ചെയ്യലും അനുഭവപരിശോധനയും ചേർന്ന് അപ്ലിക്കേഷൻ മേഖലയിലെ വിദഗ്ധതയും ശിപാർശചെയ്ത സാങ്കേതിക വിദ്യകളും മോഡൽ-നിർദ്ദിഷ്ട ആപ്റ്റിമൈസേഷനുകളും ഉൾക്കൊള്ളുന്ന ഒരു പരീക്ഷണ രീതിയാണ്.

ഈ പാഠവുമായി ചേർന്നിരിക്കുന്ന ജ്യൂപിറ്റർ നോട്ട്‌ബുക്ക് ഒരു _സാമ്പ്‌ബോക്സ്_ പരിസ്ഥിതി ആണ്, ഇവിടെ നിങ്ങൾ പഠിച്ചവ പരിചയപ്പെടുത്താം - തുടർന്നോ സെഷന്റെ ഭാഗമായ ചോദ്യം-ഉത്തരം ഭാഗമായോ.  
പരീക്ഷണങ്ങൾ നടപ്പിൽ ചെലുത്താൻ പ്രതീക്ഷിക്കപ്പെടുന്നത്:  
1. **ഒരു Azure OpenAI API കീ** - ഡിപ്ലോയിംഗ് ചെയ്ത LLM-യുടെ സേവന എൻഡ്പോയിന്റ്.  
2. **പPython റൺടൈം** - നോട്ട്‌ബുക്ക് പ്രവര്‍ത്തിപ്പിക്കാൻ.  
3. **ലോകൽ എൻവൈറൺമെന്റ് വേരിയബിളുകൾ** -  [SETUP](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) പടികളുമായി ഇപ്പോൾ തയ്യാറാകുക.

നോട്ട്ബുക്ക് _സ്റ്റാർട്ടർ_ പരീക്ഷണങ്ങളോടെയാണ് എത്തുന്നത് - പക്ഷെ നിങ്ങൾക്ക് നിങ്ങളുടെ സ്വന്തം _മാർക്ക്‌ഡൗൺ_ (വിവരണം)യും _കോഡ്_ (പ്രോംപ്‌റ് അഭ്യർത്ഥനകൾ) വിഭാഗങ്ങളും ചേർത്ത് കൂടുതൽ ഉദാഹരണങ്ങൾ പരീക്ഷിക്കാൻ പങ്കാളിയാകാം, ഈ പ്രോംപ്‌റ്റ് രൂപകൽപനക്ക് നിങ്ങളുടെ ക്ലേശം വർദ്ധിപ്പിക്കാം.

## വാസ്തവ ദൃശ്യ നിർദ്ദേശകം

ഈ പാഠം എന്തൊക്കെ ഉൾപ്പെടുന്നതെന്ന് വലിയ ദൃശ്യരൂപംകൊണ്ട് നോക്കാൻ ആഗ്രഹമുണ്ടോ? ഈ ദൃശ്യ നിർദ്ദേശകം പ്രധാന വിഷയങ്ങളും നിങ്ങൾക്ക് ചിന്തിക്കാൻ പ്രധാനപ്പെട്ട കാര്യങ്ങളും നമ്മുക്ക് നൽകുന്നു. ഈ പാഠപഥം മുഖ്യ ആശയങ്ങളെയും പ്രശ്നങ്ങളെയും മനസിലാക്കി അനുയോജ്യമായ പ്രോംപ്‌റ്റ് എഞ്ചിനീയറിംഗ് സാങ്കേതിക വിദ്യകളും മികച്ച പ്രവർത്തനരീതികളും ഉപയോഗപ്പെടുത്തുന്നതിലേക്ക് നിങ്ങളെ നയിക്കുന്നു. ഈ നിർദ്ദേശകത്തിലെ "അധിപ്രമുഖ സാങ്കേതിക വിദ്യകൾ" വിഭാഗം ഈ പാഠപദ്ധതിയുടെ അടുത്ത അധ്യായത്തിൽ ഉൾപ്പെടുന്ന ഉള്ളടക്കത്തിലേക്ക് സൂചിപ്പിക്കുന്നു.

![പ്രോംപ്‌റ്റ് എഞ്ചിനീയറിംഗിന് ദൃശ്യ നിർദ്ദേശകം](../../../translated_images/ml/04-prompt-engineering-sketchnote.d5f33336957a1e4f.webp)

## ഞങ്ങളുടെ സ്റ്റാർട്ടപ്പ്

ഇപ്പോൾ, _ഈ വിഷയം_ [വിദ്യാഭ്യാസത്തിലേക്ക് എ.ഐ. നവീകരണം കൊണ്ടുവരുന്നതിനുള്ള](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst) നമ്മുടെ സ്റ്റാർട്ടപ്പ് ദൗത്യം എങ്ങനെ ബന്ധപ്പെട്ടിരിക്കുന്നു എന്ന് നോക്കാം.  
ഞങ്ങൾ _വ്യക്തിഗത പഠനത്തിലും_ എ.ഐ. പിന്തുണയുള്ള ആപ്പുകൾ സൃഷ്ടിക്കാനാഗ്രഹിക്കുന്നു - അതിനാൽ വിവിധ ഉപയോക്താക്കൾ നമ്മുടെ ആപ്ലിക്കേഷനിൽ എങ്ങനെ "പ്രോംപ്‌റുകൾ ഡിസൈൻ" ചെയ്യുന്നതായി ചിന്തിക്കാം:

- **അഡ്മിനിസ്ട്രേറ്ററുകൾ** എ.ഐ.യ്ക്ക് _പാഠ്യപദ്ധതി ഡാറ്റ പരിശോധിച്ച് കവർ ചെയ്യാത്ത ഭാഗങ്ങൾ കണ്ടെത്താൻ_ സഹായം ആവശ്യമുണ്ടാകും. എ.ഐ. ഫലങ്ങൾ സംഗ്രഹിപ്പിക്കുക അല്ലെങ്കിൽ കോഡുപയോഗിച്ച് ദൃശ്യീകരിക്കാം.  
- **ശിക്ഷകർ** എ.ഐ. ആവശ്യപ്പെടും _കുറ്റിച്ചറിയിച്ച പ്രേക്ഷകർക്കും വിഷയത്തിനും അനുയോജ്യമായ പാഠ പദ്ധതി തയാറാക്കാൻ_. എ.ഐ. വ്യക്തിഗത കഥ കേസ് നൽകിയ ഫോർമാറ്റിൽ പാഠ പദ്ധതി സൃഷ്ടിക്കും.  
- **വിദ്യാർത്ഥികൾ** എ.ഐ. ചോദ്യപ്പെടും _ഒരു ദുഷ്‌കര വിഷയം പഠിപ്പിക്കാൻ_. എ.ഐ. ഇപ്പോള്‍ പാഠങ്ങൾ, സന്ദേശങ്ങൾ & ഉദാഹരണങ്ങൾ അവരുടെ നിലവാരത്തിനനുസരിച്ച് കുട്ടികള്ക്ക് മാർഗ്ഗനിർദ്ദേശം നൽകുന്നു.

വിലാപത്തിനിടയിലെ ഒരു കൊമ്പിലാണ് ഇത്. [വിദ്യാഭ്യാസത്തിനായി പ്രോംപ്‌റുകൾ](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) എന്ന ഒരു ഓപ്പൺ സോഴ്സ് പ്രോംപ്‌റ്റ് ലൈബ്രറി പരിചയപ്പെടുക - വിദ്യാഭ്യാസ വിദഗ്ധർ സംഗ്രഹിച്ചിരിക്കുന്നതും സാധ്യതകൾ കൂടുതലായി മനസ്സിലായിപ്പോകുന്നുമുണ്ട്! _അവിടെ കുറച്ചുകാര്യങ്ങൾ സാൻഡ്‌ബോക്സിൽ പരീക്ഷിക്കുക അല്ലെങ്കിൽ OpenAI പ്ലേഗ്രൗണ്ട് ഉപയോഗിച്ച് നോക്കുക, എന്തൊക്കെ ഫലങ്ങളുണ്ടാകുന്നു എന്ന് കണ്ടാലും!_

<!--  
LESSON TEMPLATE:  
This unit should cover core concept #1.  
Reinforce the concept with examples and references.

CONCEPT #1:  
Prompt Engineering.  
Define it and explain why it is needed.  
-->

## പ്രോംപ്‌റ്റ് എഞ്ചിനീയറിംഗ് എന്താണ്?

ഈ പാഠം തുടങ്ങിയപ്പോൾ ഞങ്ങൾ **പ്രോംപ്‌റ്റ് എഞ്ചിനീയറിംഗ്** എന്നത് ഒരു ഉൾക്കാഴ്ചയായി നിർമ്മിക്കുകയും ആപ്ലിക്കേഷൻ ലക്ഷ്യത്തിനും മോഡലിനും അനുയോജ്യമായ ഫലപ്രദമായ പ്രതികരണങ്ങൾ (കമ്പ്ലീഷന്‍സ്) നൽകാൻ ടെക്സ്റ്റ് ഇൻപുട്ടുകൾ (പ്രോംപ്‌റുകൾ) രൂപകൽപ്പന ചെയ്ത് മെച്ചപ്പെടുത്തൽ എന്ന രീതിയിലാണ് പരിഗണിച്ചത്. ഇതിനെ രണ്ട് ഘട്ട പ്രക്രിയയായി ചിന്തിക്കാം:

- ഒരു മോഡലിനും ലക്ഷ്യത്തിനും അനുയോജ്യമായ ആദ്യ പ്രോംപ്‌റ് _രൂപകല്പനം_ ചെയ്യുക  
- പുനരാവൃത്തിയായി പ്രോംപ്‌റ് _മെച്ചപ്പെടുത്തുക_ പ്രതികരണ ഗുണമേന്മ മെച്ചപ്പെടുത്താൻ

ഇത് ആവശ്യം കൊണ്ട് നിരന്തരം പരിശോധന ചെയ്യേണ്ട പ്രക്രിയയാണ്, ഉപയോക്താവിന് അനുഭാവവും പരിശ്രമവും വേണം മികച്ച ഫലങ്ങൾ ലഭിക്കാൻ. എന്നാൽ ഇതിന് പ്രാധാന്യമുണ്ടോ? ഉത്തരം അറിയാൻ നാം ആദ്യം മൂന്ന് ആശയങ്ങൾ മനസ്സിലാക്കണം:

- _ടോകനൈസേഷൻ_ = മോഡൽ പ്രോംപ്‌റിനെ എങ്ങനെ "കാണുന്നു"  
- _ബേസ് LLMകൾ_ = അടിസ്ഥാന മോഡൽ എങ്ങനെ പ്രോംപ്‌റിനെ "പ്രോസസ്സ്" ചെയ്യുന്നു  
- _ഇൻസ്റ്റ്രക്ഷൻ-ട്യൂൺ ചെയ്ത LLMകൾ_ = മോഡൽ എങ്ങനെ "പ്രവൃത്തികൾ" കാണാൻ കഴിയും

### ടോകനൈസേഷൻ

ഒരു LLM പ്രോംപ്‌റുകൾ _ടോകൺസ് എന്ന അനന്തരവ(sequence)_ ആയി കാണുന്നു, ഓരോ മോഡലും (അല്ലെങ്കിൽ ഒരു മോഡലിന്റെ വ്യത്യസ്ത പതിപ്പുകളും) ഒരേ പ്രോംപ്‌റിന് വ്യത്യസ്ത രീതിയിൽ ടോകനൈസ് ചെയ്യാവുന്നതാണ്. LLMകൾ ടോകണുകളിൽ പരിശീലനമേൽക്കുന്നതുകൊണ്ട് (റോ ടെക്സ്റ്റിൽ അല്ല), പ്രോംപ്‌റുകൾ എങ്ങനെ ടോകനൈസ് ചെയ്യപ്പെടുന്നു എന്നത് സൃഷ്ടിക്കുന്ന പ്രതികരണത്തിന്റെ ഗുണമേന്മയിൽ നേരിട്ടുള്ള സ്വാധീനമുണ്ട്.

ടോകനൈസേഷൻ എങ്ങനെ പ്രവർത്തിക്കുന്നു എന്ന് മനസ്സിലാക്കാൻ, താഴെ കാണുന്ന പോലെ [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) പോലുള്ള ഉപകരണങ്ങൾ പരീക്ഷിക്കുക. നിങ്ങളുടെ പ്രോംപ്‌റ് പകർത്തി ഒട്ടിക്കുക - അത് എങ്ങനെ ടോകണുകളായി മാറുന്നു എന്നതും, വെളിപ്പെടുത്താത്ത പങ്കുകളും പഞ്ചുകൾ എങ്ങനെ കൈകാര്യം ചെയ്യപ്പെടുകയാണ് എന്നതും ശ്രദ്ധിക്കുക. ഈ ഉദാഹരണം പഴയ LLM (GPT-3) കാണിക്കുന്നു - പുതിയ മോഡലിൽ പരീക്ഷിക്കുന്നതിൽ വ്യത്യാസങ്ങൾ കാണാം.

![ടോക്കനൈസേഷൻ](../../../translated_images/ml/04-tokenizer-example.e71f0a0f70356c5c.webp)

### ആശയം: ഫൗണ്ടേഷൻ മോഡലുകൾ

ഒരു പ്രോംപ്‌റ് ടോകണുകളായി മാറിയവബ്രൂല, ["ബേസ് LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (അഥവാ ഫൗണ്ടേഷൻ മോഡൽ) അതിന്റെ പ്രധാന പ്രവർത്തനം ആ ടോകൺ അനന്തരവത്തിൽ അടുത്ത ടോകൺ പ്രവചിക്കുന്നതാണ്. വലിയ ടെക്സ്റ്റ് ഡാറ്റാസെറ്റുകളിൽ പരിശീലനം ലഭിച്ചതിനാൽ, അവയ്ക്ക് ടോകണുകൾ തമ്മിലുള്ള സ്ഥിതിസംബന്ധങ്ങളെ അഭിമുഖീകരിച്ച് വിശ്വാസത്തോടെ പ്രവചനം നടത്താൻ കഴിയും. അവർ പ്രോംപ്‌റിലെ വാക്കുകളുടെ _അർത്ഥം_ മനസ്സിലാക്കുന്നില്ല; ഒരു പാറ്റേൺ കാണുന്നു, അതു അവരുടെ അടുത്ത പ്രവചനത്തോടെ "പൂർത്തിയാക്കാം". ഉപയോക്താവിന്റെ ഇടപെടലോ നിർണ്ണയിച്ച നിബന്ധനകളോ വന്നില്ലെങ്കിൽ, അവർ അത്തരമൊരു അനുശ Virgin മഴം തുടരം .

പ്രോംപ്‌റ്റ് അടിസ്ഥാനമാക്കിയുളള കമ്പ്ലീഷൻ എങ്ങിനെ പ്രവർത്തിക്കുന്നു എന്ന് കാണാൻ ആഗ്രഹമുണ്ടോ? മുമ്പിൽ ചേർത്ത പ്രോംപ്‌റ് Azure OpenAI സ്റ്റുഡിയോ [_ചാറ്റ് പ്ലേഗ്രൗണ്ട്_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) ലെ ഡിഫോൾട്ട് ഘടനയിൽ നൽകുക. സിസ്റ്റം പ്രോംപ്‌റുകളെ വിവര അഭ്യർത്ഥനകൾ ആയി പരിഗണിക്കുന്നതിനാൽ നിങ്ങൾക്ക് ഇതിനു സാക്ഷ്യമായ ഒരു പ്രതികരണം കാണാം.

പക്ഷെ ഒരു ഉപയോക്താവ് ചില മാനദണ്ഡങ്ങൾക്കും ലക്ഷ്യങ്ങൾക്ക് അനുയോജ്യമായ പ്രത്യേക പ്രതീക്ഷകളുള്ള കാര്യങ്ങൾ കാണാനാഗ്രഹിക്കുകയാണെങ്കിൽ? ആ ഘട്ടത്തിൽ _ഇൻസ്റ്റ്രക്ഷൻ-ട്യൂൺഡ്_ LLMകൾ സജീവമാകുന്നു.

![ബേസ് LLM ചാറ്റ് കമ്പ്ലീഷൻ](../../../translated_images/ml/04-playground-chat-base.65b76fcfde0caa67.webp)

### ആശയം: ഇൻസ്റ്റ്രക്ഷൻ ട്യൂൺ ചെയ്ത LLMകൾ

[ഇൻസ്റ്റ്രക്ഷൻ ട്യൂൺഡ് LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) എങ്കിൽ ഫൗണ്ടേഷൻ മോഡലിലൂടെ ആരംഭിച്ച് ഉദാഹരണങ്ങളിലൂടെയോ ഇൻപുട്ട്/ഔട്ട്‌പുട്ട് ജോഡികൾ (ഉദാ: മൾട്ടി-ടേൺ "സന്ദേശങ്ങൾ") വഴി ഫൈനൽ-ട്യൂൺ ചെയ്തതാണ്, അവ വ്യക്തമായ നിർദ്ദേശങ്ങൾ ഉൾക്കൊള്ളുന്നു - എ.ഐ. അവ അനുസരിക്കാൻ ശ്രമിക്കുന്നു.

ഈ പാക്കേജ് Reinforcement Learning with Human Feedback (RLHF) പോലുള്ള സാങ്കേതിക വിദ്യകൾ ഉപയോഗിക്കുന്നു, അതിലൂടെ മോഡൽ _നിർദ്ദേശം പാലിക്കാൻ_ പഠിക്കുന്നു, _ഫീഡ്ബാക്കിൽ നിന്ന് പഠിക്കുന്നു_ എന്നിങ്ങനെ, ഫലമായി മോഡൽ നൽകുന്ന പ്രതികരണങ്ങൾ പ്രായോഗിക ആപ്ലിക്കേഷനുകൾക്കും ഉപയോക്തൃ ലക്ഷ്യങ്ങൾക്കും കൂടുതൽ അനുയോജ്യമായതാകുന്നു.

അതിന്റെ സൂചനയ്ക്ക് മുമ്പത്തെ പ്രോംപ്‌റ് വീണ്ടും ഉപയോഗിക്കാം, പക്ഷേ _സിസ്റ്റം സന്ദേശം_ താഴെ പറയുന്ന നിർദ്ദേശം പോലെ മാറ്റുക:

> _നിങ്ങൾ ലഭിക്കുന്ന ഉള്ളടക്കം ഒരു രണ്ടാം ക്ലാസ് കുട്ടിക്ക് സങ്ക്ഷിപ്തമാക്കുക. ഫലത്തെ ഒരു പാരഗ്രാഫിൽ 3-5 ബുള്ളറ്റ് പോയിന്റുകളിലാക്കി വെക്കുക._

ഫലം ഇപ്പോൾ ആഗ്രഹിച്ച ലക്ഷ്യം ഒപ്പം ഫോർമാറ്റിനേയും പരിഗണിച്ചുള്ളതാകുന്നുവെന്ന് കാണുക. ഒരു അധ്യാപകന് ഈ പ്രതികരണം തങ്ങളുടെ ക്ലാസിനു വേണ്ട സ്ലൈഡുകളിൽ നേരിട്ട് ഉപയോഗിക്കാം.

![ഇൻസ്റ്റ്രക്ഷൻ ട്യൂൺഡ് LLM ചാറ്റ് കമ്പ്ലീഷൻ](../../../translated_images/ml/04-playground-chat-instructions.b30bbfbdf92f2d05.webp)

## എന്തുകൊണ്ടാണ് പ്രോംപ്‌റ്റ് എഞ്ചിനീയറിംഗ് ആവശ്യമുള്ളത്?

ഇപ്പോൾ നമുക്ക് LLMകൾ പ്രോംപ്‌റുകൾ എങ്ങനെ പ്രോസസ്സ് ചെയ്യുന്നു എന്നും മനസ്സിലായി. എങ്കിൽ _എന്തിനാണ്_ പ്രോംപ്‌റ്റ് എഞ്ചിനീയറിംഗ് ആവശ്യമെന്ന് നോക്കാം.  
നിലവിലെ LLMകൾ വിവിധ വെല്ലുവിളികൾ നിമിത്തം _നിഷ്പക്ഷവും സ്ഥിരതയുള്ളതുമായ കമ്പ്ലീഷനുകൾ_ കുറഞ്ഞ ശ്രമത്തോടെ ലഭിക്കുന്നതിന് പ്രോംപ്‌റ് രൂപകൽപ്പനയും മെച്ചപ്പെടുത്തലും അനിവാര്യമായി ആവശ്യമാണ്. ഉദാഹരണങ്ങൾക്ക്:

1. **മോഡൽ പ്രതികരണങ്ങൾ സഞ്ചിതമാറ്റം ഉള്ളതാണ്.** _അതിനേകം പ്രോംപ്‌റ്_ വ്യത്യസ്ത മോഡലുകളും പതിപ്പുകളും ഉപയോഗിക്കുന്നു വെല്ലുവിളി വന്നു വരുന്ന തരത്തിലാണ്. ഒരു മോഡലിലേതും സമയത്തിന്റെയും ആശയഭേദം വരാം. _പ്രോംപ്‌റ്റ് എഞ്ചിനീയറിംഗ് സാങ്കേതിക വിദ്യകൾ ഈ അവ്യക്തത കുറയ്ക്കുന്നതിനും മികച്ച നിയന്ത്രണങ്ങൾ നൽകുന്നതിനും സഹായിക്കുന്നു_.

2. **മോഡലുകൾ തെറ്റായ പ്രതികരണങ്ങൾ സൃഷ്ടിക്കാം.** മോഡലുകൾ _വലിയ പക്ഷെ പരിമിതമായ_ ഡാറ്റാസെറ്റുകളിൽ പരിശീലനം ഉള്ളതിനാൽ പരിശീലന പരിധിയേക്കാൾ പുറത്തുള്ള ധാരണകൾക്കുറിച്ചു അവയ്ക്ക് അറിവ് കുറവുണ്ട്. അതിനാൽ അവർ തെറ്റായ, സങ്കല്പാത്മക, അല്ലെങ്കിൽ സത്യവാങ്മൂലങ്ങളോട് വിരുദ്ധമായ പ്രതിമുഖങ്ങൾ സൃഷ്ടിക്കാം. _പ്രോംപ്‌റ്റ് എഞ്ചിനീയറിംഗ് ഉപയോക്താക്കളെ ഇത്തരം തെറ്റികളെ തിരിച്ചറിയാനും അത് കുറക്കാനും സഹായിക്കുന്നു, ഉദാഹരണത്തിന്, AI-യെ സിലുംഷനങ്ങൾക്കും ന്യായീകരണങ്ങൾക്കും ചോദിക്കുക._

3. **മോഡൽ കഴിവുകൾ വ്യത്യാസപ്പെടും.** പുതിയ മോഡലകൾ കൂടുതൽ ശേഷികളോടെ കൂടി എത്തും, എന്നാൽ ചില പ്രത്യേകതകളിൽ വ്യത്യാസങ്ങൾയും ചെലവും സങ്കീർണ്ണതയും വരുത്തും. _പ്രോംപ്‌റ്റ് എഞ്ചിനീയറിംഗ് ശരിയായ അഭ്യാസങ്ങളും പ്രവൃത്തി പ്രവണതകളും വികസിപ്പിച്ച് മോഡൽ വ്യതിയാനങ്ങൾ മറക്കാനുള്ള വഴികളും, scalabilityഉം സുതാര്യതയും ഉറപ്പുവരുത്തുന്ന ഉപാധികളായി മാറുന്നു_.

ഇത് OpenAI അല്ലെങ്കിൽ Azure OpenAI പ്ലേഗ്രൗണ്ടിൽ പ്രയോഗിക്കാം:  

- വ്യത്യസ്ത LLM ഡിപ്ലോയ്മെന്റുകൾ (ഉദാ. OpenAI, Azure OpenAI, Hugging Face) ഉദാഹരണത്തിന് ഒരേ പ്രോംപ്‌റ് നൽകൂ - വ്യത്യാസങ്ങൾ കാണുമോ?  
- ഒരേ LLM ഡിപ്ലോയ്മെന്റിൽ (ഉദാ Azure OpenAI പ്ലേഗ്രൗണ്ട്) ഒരേ പ്രോംപ്‌റ് പല പ്രാവശ്യം ഉപയോഗിക്കൂ - വ്യത്യാസങ്ങൾ എങ്ങനെ വ്യത്യസ്തമാണ്?

### തെറ്റായ റിപ്പോർട്ടുകളുടെ ഉദാഹരണം

ഈ കോഴ്സിൽ "**ഫബ്രിക്കേഷൻ**" എന്ന പദം LLMകൾ ചിലപ്പോൾ പരിശീലനപരിധിയിലെ മൂല്യഭേദങ്ങൾ അല്ലെങ്കിൽ മറ്റു പരിധികൾ മൂലം സത്യമല്ലാത്ത വിവരങ്ങൾ സൃഷ്ടിക്കുന്ന അവസ്ഥയെ സൂചിപ്പിക്കാൻ ഉപയോഗിക്കുന്നു. പൊതുപ്രചാരത്തിലുള്ള ലേഖനങ്ങളിലും ഗവേഷണപത്രങ്ങളിലും ഇത് _"ഹാല്യൂസിനേഷൻസ്"_ എന്നും വിളിക്കപ്പെടാറുണ്ട്. എന്നാൽ ഇതിന് പകരം _"ഫബ്രിക്കേഷൻ"_ എന്ന പദം ഉപയോഗിക്കാൻ ഞങ്ങൾ ശേഷിക്കുന്നു, അതിനാൽ യന്ത്രം സൃഷ്ടിക്കുന്ന ഒരു ഫലത്തെ മനുഷ്യപോലെ ലിംഗവിവരമുള്ള സ്വഭാവം നൽകുന്ന തെറ്റായ ചിത്രീകരണം ഒഴിവാക്കാം. ഇത് [ജാഗ്രതയോടെ എ.ഐ. വഴി നിർദേശം നൽകാൻ](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) വേണ്ട ടെർമിനോളജിയിൽ പരിഗണിക്കപ്പെടുന്നു, ചില സാഹചര്യങ്ങളിൽ അപമാനകരമോ ഉൾക്കൊള്ളാത്തതുമായ പദങ്ങൾ ഒഴിവാക്കുന്നു.

ഫബ്രിക്കേഷനുകൾ എങ്ങനെ പ്രവർത്തിക്കുന്നുവെന്ന് അറിയാൻ ആഗ്രഹമുണ്ടോ?  
അതിനായി AI-യെ ഒരു സൃഷ്ടിച്ചിട്ടില്ലാത്ത വിഷയത്തിൽ ഉള്ളടക്കം ഉത്പാദിപ്പിക്കാൻ നിർദേശിക്കുന്ന പ്രോംപ്‌റ് കരുതൂ (പഠന ഡാറ്റാസെറ്റിൽ ഇല്ലാതിരിക്കണം). ഉദാഹരണത്തിന് - ഞാൻ ഈ പ്രോംപ്‌റ് പരീക്ഷിച്ചു:

> **പ്രോംപ്‌റ്:** 2076ലെ മാർഷ്യൻ യുദ്ധത്തെക്കുറിച്ച് ഒരു പാഠ പദ്ധതി നാല്‍കുക.
A web search showed me that there were fictional accounts (e.g., television series or books) on Martian wars - but none in 2076. Commonsense also tells us that 2076 is _in the future_ and thus, cannot be associated with a real event.

So what happens when we run this prompt with different LLM providers?

> **Response 1**: OpenAI Playground (GPT-35)

![Response 1](../../../translated_images/ml/04-fabrication-oai.5818c4e0b2a2678c.webp)

> **Response 2**: Azure OpenAI Playground (GPT-35)

![Response 2](../../../translated_images/ml/04-fabrication-aoai.b14268e9ecf25caf.webp)

> **Response 3**: : Hugging Face Chat Playground (LLama-2)

![Response 3](../../../translated_images/ml/04-fabrication-huggingchat.faf82a0a51278956.webp)

As expected, each model (or model version) produces slightly different responses thanks to stochastic behavior and model capability variations. For instance, one model targets an 8th grade audience while the other assumes a high-school student. But all three models did generate responses that could convince an uninformed user that the event was real.

Prompt engineering techniques like _metaprompting_ and _temperature configuration_ may reduce model fabrications to some extent. New prompt engineering _architectures_ also incorporate new tools and techniques seamlessly into the prompt flow, to mitigate or reduce some of these effects.

## Case Study: GitHub Copilot

Let's wrap this section by getting a sense of how prompt engineering is used in real-world solutions by looking at one Case Study: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot is your "AI Pair Programmer" - it converts text prompts into code completions and is integrated into your development environment (e.g., Visual Studio Code) for a seamless user experience. As documented in the series of blogs below, the earliest version was based on the OpenAI Codex model - with engineers quickly realizing the need to fine-tune the model and develop better prompt engineering techniques, to improve code quality. In July, they [debuted an improved AI model that goes beyond Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) for even faster suggestions.

Read the posts in order, to follow their learning journey.

- **May 2023** | [GitHub Copilot is Getting Better at Understanding Your Code](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **May 2023** | [Inside GitHub: Working with the LLMs behind GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Jun 2023** | [How to write better prompts for GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Jul 2023** | [.. GitHub Copilot goes beyond Codex with improved AI model](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Jul 2023** | [A Developer's Guide to Prompt Engineering and LLMs](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Sep 2023** | [How to build an enterprise LLM app: Lessons from GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

You can also browse their [Engineering blog](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) for more posts like [this one](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst) that shows how these models and techniques are _applied_ for driving real-world applications.

---

<!--
LESSON TEMPLATE:
This unit should cover core concept #2.
Reinforce the concept with examples and references.

CONCEPT #2:
Prompt Design.
Illustrated with examples.
-->

## Prompt Construction

We've seen why prompt engineering is important - now let's understand how prompts are _constructed_ so we can evaluate different techniques for more effective prompt design.

### Basic Prompt

Let's start with the basic prompt: a text input sent to the model with no other context. Here's an example - when we send the first few words of the US national anthem to the OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst) it instantly _completes_ the response with the next few lines, illustrating the basic prediction behavior.

| Prompt (Input)     | Completion (Output)                                                                                                                        |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | It sounds like you're starting the lyrics to "The Star-Spangled Banner," the national anthem of the United States. The full lyrics are ... |

### Complex Prompt

Now let's add context and instructions to that basic prompt. The [Chat Completion API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) lets us construct a complex prompt as a collection of _messages_ with:

- Input/output pairs reflecting _user_ input and _assistant_ response.
- System message setting the context for assistant behavior or personality.

The request is now in the form below, where the _tokenization_ effectively captures relevant information from context and conversation. Now, changing the system context can be as impactful on the quality of completions, as the user inputs provided.

```python
response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
```

### Instruction Prompt

In the above examples, the user prompt was a simple text query that can be interpreted as a request for information. With _instruction_ prompts, we can use that text to specify a task in more detail, providing better guidance to the AI. Here's an example:

| Prompt (Input)                                                                                                                                                                                                                         | Completion (Output)                                                                                                        | Instruction Type    |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Write a description of the Civil War                                                                                                                                                                                                   | _returned a simple paragraph_                                                                                              | Simple              |
| Write a description of the Civil War. Provide key dates and events and describe their significance                                                                                                                                     | _returned a paragraph followed by a list of key event dates with descriptions_                                             | Complex             |
| Write a description of the Civil War in 1 paragraph. Provide 3 bullet points with key dates and their significance. Provide 3 more bullet points with key historical figures and their contributions. Return the output as a JSON file | _returns more extensive details in a text box, formatted as JSON that you can copy-paste to a file and validate as needed_ | Complex. Formatted. |

## Primary Content

In the above examples, the prompt was still fairly open-ended, allowing the LLM to decide what part of its pre-trained dataset was relevant. With the _primary content_ design pattern, the input text is divided into two parts:

- an instruction (action)
- relevant content (that influences action)

Here's an example where the instruction is to "summarize this in 2 sentences".

| Prompt (Input)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Completion (Output)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jupiter is the fifth planet from the Sun and the largest in the Solar System. It is a gas giant with a mass one-thousandth that of the Sun, but two-and-a-half times that of all the other planets in the Solar System combined. Jupiter is one of the brightest objects visible to the naked eye in the night sky, and has been known to ancient civilizations since before recorded history. It is named after the Roman god Jupiter.[19] When viewed from Earth, Jupiter can be bright enough for its reflected light to cast visible shadows,[20] and is on average the third-brightest natural object in the night sky after the Moon and Venus. <br/> **Summarize this in 2 short sentences** | Jupiter, the fifth planet from the Sun, is the largest in the Solar System and is known for being one of the brightest objects in the night sky. Named after the Roman god Jupiter, it's a gas giant whose mass is two-and-a-half times that of all other planets in the Solar System combined. |

The primary content segment can be used in various ways to drive more effective instructions:

- **Examples** - instead of telling the model what to do with an explicit instruction, give it examples of what to do and let it infer the pattern.
- **Cues** - follow the instruction with a "cue" that primes the completion, guiding the model towards more relevant responses.
- **Templates** - these are repeatable 'recipes' for prompts with placeholders (variables) that can be customized with data for specific use cases.

Let's explore these in action.

### Using Examples

This is an approach where you use the primary content to "feed the model" some examples of the desired output for a given instruction, and let it infer the pattern for the desired output. Based on the number of examples provided, we can have zero-shot prompting, one-shot prompting, few-shot prompting etc.

The prompt now consists of three components:

- A task description
- A few examples of the desired output
- The start of a new example (which becomes an implicit task description)

| Learning Type | Prompt (Input)                                                                                                                                        | Completion (Output)         |
| :------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------- |
| Zero-shot     | "The Sun is Shining". Translate to Spanish                                                                                                            | "El Sol está brillando".    |
| One-shot      | "The Sun is Shining" => ""El Sol está brillando". <br> "It's a Cold and Windy Day" =>                                                                 | "Es un día frío y ventoso". |
| Few-shot      | The player ran the bases => Baseball <br/> The player hit an ace => Tennis <br/> The player hit a six => Cricket <br/> The player made a slam-dunk => | Basketball                  |
|               |                                                                                                                                                       |                             |

Note how we had to provide explicit instruction ("Translate to Spanish") in zero-shot prompting, but it gets inferred in the one-shot prompting example. The few-shot example shows how adding more examples allows models to make more accurate inferences with no added instructions.

### Prompt Cues

Another technique for using primary content is to provide _cues_ rather than examples. In this case, we are giving the model a nudge in the right direction by _starting it off_ with a snippet that reflects the desired response format. The model then "takes the cue" to continue in that vein.

| Number of Cues | Prompt (Input)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Completion (Output)                                                                                                                                                                                                                                                                                       |
| :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0              | Jupiter is the fifth planet from the Sun and the largest in the Solar System. It is a gas giant with a mass one-thousandth that of the Sun, but two-and-a-half times that of all the other planets in the Solar System combined. Jupiter is one of the brightest objects visible to the naked eye in the night sky, and has been known to ancient civilizations since before recorded history. <br/>**Summarize This**                                       | Jupiter is the largest planet in our Solar System and the fifth one from the Sun. It is a gas giant with a mass 1/1000th of the Sun's, but it is heavier than all the other planets combined. Ancient civilizations have known about Jupiter for a long time, and it is easily visible in the night sky.. |
| 1              | ജൂപ്പിറ്റർ സൂര്യനിൽ നിന്നും അഞ്ചാമത്തെ ഗ്രഹവും നമ്മുടെ സോളാർ സിസ്റ്റത്തിലെ ഏറ്റവും വലിയ ഗ്രഹവുമാണ്. സൂര്യനേക്കാൾ ഒരു ആയിരം വർഷം കുറഞ്ഞ ഭാരം ഉള്ള ഒരു വാതക ഗോലം ആണ് ഇത്, എന്നാൽ സോളാർ സിസ്റ്റത്തിലെ മറ്റു എല്ലാ ഗ്രഹങ്ങളുടെയും ഭാരം ചേർന്നുള്ളതിന്റെ ഇരട്ടിയ്ക്കും കുറച്ച് കവല ഇതിനുണ്ട്. നിശാന്തരങ്ങളിൽ സൂക്ഷ്മദൃശ്യമാനമായ ഏറ്റവും പ്രകാശവാനായ വസ്തുക്കളുടെ ഒന്നാണ് ജൂപ്പിറ്റർ, നിരവധി പുരാതന സംസ്കാരങ്ങൾ ഇതിനെ രചിത ചരിത്രത്തിനുമുന്പ് അറിയാമായിരുന്നു. <br/>**ചുരുക്കിപ്പറയുക** <br/> ഞങ്ങൾ പഠിച്ചത് ഇതാണ്: ജൂപ്പിറ്റർ | സൂര്യനിൽ നിന്നും അഞ്ചാമത്തെ ഗ്രഹവും സോളാർ സിസ്റ്റത്തിലെ ഏറ്റവും വലിയ ഗ്രഹവുമാണ്. ഇത് ഒരു വാതക ജെനായി, സൂര്യന്റെ ഭാരത്തിന് ഒരു ആയിരം ശതമാനമായി കുറഞ്ഞതിനാലും എല്ലാ മറ്റ് ഗ്രഹങ്ങളുടെ കൂട്ട ഭാരം അതിന്റെ ഇരട്ടി കണക്കിലാണ്. ഇത് സൂക്ഷ്മദൃശ്യമാനം ആയി കാഴ്ചക്കാരനെ കാണാനാകും, പുരാതന കാലങ്ങളിൽ നിന്നെന്ന് അറിയപ്പെടുന്നു.                        |
| 2              | ജൂപ്പിറ്റർ സൂര്യനിൽ നിന്നും അഞ്ചാമത്തെ ഗ്രഹവും നമ്മുടെ സോളാർ സിസ്റ്റത്തിലെ ഏറ്റവും വലിയ ഗ്രഹവുമാണ്. സൂര്യനേക്കാൾ ഒരു ആയിരം വർഷം കുറഞ്ഞ ഭാരം ഉള്ള ഒരു വാതക ഗോലം ആണ് ഇത്, എന്നാൽ സോളാർ സിസ്റ്റത്തിലെ മറ്റു എല്ലാ ഗ്രഹങ്ങളുടെയും ഭാരം ചേർന്നുള്ളതിന്റെ ഇരട്ടിയ്ക്കും കുറച്ച് കവല ഇതിനുണ്ട്. നിശാന്തരങ്ങളിൽ സൂക്ഷ്മദൃശ്യമാനമായ ഏറ്റവും പ്രകാശവാനായ വസ്തുക്കളുടെ ഒന്നാണ് ജൂപ്പിറ്റർ, നിരവധി പുരാതന സംസ്കാരങ്ങൾ ഇതിനെ രചിത ചരിത്രത്തിനുമുന്പ് അറിയാമായിരുന്നു. <br/>**ചുരുക്കിപ്പറയുക** <br/> മുകളിൽ പഠിച്ച 3 പ്രധാന വസ്തുക്കൾ:         | 1. ജൂപ്പിറ്റർ സൂര്യനിൽ നിന്നും അഞ്ചാമത്തെ ഗ്രഹവും സോളാർ സിസ്റ്റത്തിലെ ഏറ്റവും വലിയ ഗ്രഹവുമാണ്. <br/> 2. ഇത് സൂര്യന്റെ ഭാരത്തിന് ഒരു ആയിരം ശതമാനമായി കുറഞ്ഞ ഒരു വാതക ജാഗ്രത ആണ്...<br/> 3. ജൂപ്പിറ്റർ പുരാതന കാലങ്ങളിൽ മുതൽ സൂക്ഷ്മദൃശ്യമാനമായിരുന്നു ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### പ്രോംപ്റ്റ് ടെംപ്ലേറ്റുകൾ

ഒരു പ്രോംപ്റ്റ് ടെംപ്ലേറ്റ് എന്നത് ആവശ്യമായപ്പോൾ നിലനിർത്തി ഉപയോഗിക്കാവുന്ന _പূർവനിർവചിത പദാർത്ഥം_ ആണ്, ഇത് വലിയ ഉപയോക്തൃ അനുഭവങ്ങളുടെ സ്ഥിരത ഉറപ്പുവരുത്തുന്നതിനായി ഉപയോഗിക്കാം. അതിന്റെ ഏറ്റവും ലളിതമായ രൂപത്തിൽ, ഇത് ചെറിയ ഉദാഹരണങ്ങളുടെ സമാഹാരമായിരിക്കും, ഉദാ: [OpenAIയിൽ നിന്നുള്ള ഈ ഉദാഹരണം](https://cookbook.openai.com/examples/gpt4-1_prompting_guide?WT.mc_id=academic-105485-koreyst) - ഇത് user, system സന്ദേശങ്ങൾ ഉൾപ്പെടെ ഇന്ററാക്ടീവ് പ്രോംപ്റ്റ് ഘടകങ്ങളും API-വഴിയുള്ള അഭ്യർത്ഥന ഫോർമേറ്റും നൽകുന്നു, പുനരുപയോഗം പിന്തുണയ്ക്കാൻ.

LangChain-ൽ കാണുന്ന പോലെ,[LangChain-ലെ ഉദാഹരണം](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst) ഇത് _പ്ലേസ്ഹോൾഡറുകൾ_ ഉൾക്കൊള്ളുന്നു, അവ വ്യത്യസ്ത ഉറവിടങ്ങളിലെ (ഉപയോക്തൃ ഇൻപുട്ട്, സിസ്റ്റം കോൺടെക്സ്റ്റ്, പുറം ഡേറ്റ സ്രോതസ്സുകൾ മുതലായവ) ഡേറ്റ ഉപയോഗിച്ച് ഡൈനാമികായി പ്രോംപ്റ്റ് നിർമ്മിക്കാൻ ഇടയാക്കുന്നു. ഇതിലൂടെ, സാധാരണ ഉപയോഗങ്ങൾക്കായി **പ്രോഗ്രാമാറ്റിക്കായി** സ്ഥിരതയുള്ള ഉപയോക്തൃ അനുഭവങ്ങൾ സൃഷ്‌ടിക്കുന്ന പുനരുപയോഗയോഗ്യമായ പ്രോംപ്റ്റ് ലൈബ്രറികൾ സൃഷ്ടിക്കാം.

അവസാനമായി, ടെംപ്ലേറ്റിന്റെ യഥാർത്ഥ മൂല്യം തന്നെ അതിന്റെ പ്രത്യേക മേഖല ആപ്ലിക്കേഷൻ കാര്യക്ഷമതയിൽ തന്നെയാണെന്ന് പറയാം - ഉപയോക്തൃ വിഭാഗത്തിനായി കൂടുതൽ അനുയോജ്യവും കൃത്യവുമായ പ്രതികരണങ്ങൾക്കായി പ്രോംപ്റ്റ് ടെംപ്ലേറ്റുകൾ കൃത്യമായ സന്ദർഭങ്ങളും ഉദാഹരണങ്ങളും ഉൾക്കൊള്ളുന്നവയായി മെച്ചപ്പെടുത്താൻ കഴിയുന്നു. [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) റീപോസിറ്ററി ഈ സമീപനത്തിന് മികച്ച ഉദാഹരണമാണ്, വിദ്യാഭ്യാസ മേഖലയിൽ ടുട്ടറിംഗ്, പാഠ്യപദ്ധതി രൂപകൽപ്പന, ലെസൺ പ്ലാനിങ് എന്നിവയിൽ കേന്ദ്രീകരിച്ച് പ്രോംപ്റ്റ് ലൈബ്രറികൾ ശേഖരിക്കുന്നു.

## പിന്തുണയ്ക്കുന്ന ഉള്ളടക്കം

പ്രോംപ്റ്റ് നിർമ്മാണം ഒരു നിർദ്ദേശം (ജോലി) ഒപ്പം ഒരു ലക്ഷ്യം (പ്രാഥമിക ഉള്ളടക്കം) ഉള്ളതായി കരുതുമ്പോൾ, _രണ്ടാംസ്റ്റെപ്പ് ഉള്ളടക്കം_ എന്നത് ഔട്ട്പുട്ടിനെ ഒരു വിധത്തിൽ ബാധിക്കുന്ന അധിക കോൺടെക്സ്റ്റ് പോലെയാണ്. ഇത് ട്യൂണിംഗ് പാരാമീറ്ററുകൾ, ഫോർമാറ്റിംഗ് നിർദ്ദേശങ്ങൾ, വിഷയം ലോക്ക് എന്നിവയാകാം, മോഡലിനുള്ള പ്രതികരണത്തെ ഉദ്ദേശിക്കുന്ന ഉപയോക്തൃ ലക്ഷ്യങ്ങളോടോ പ്രതീക്ഷകളോടോ യോജിപ്പിക്കൽ ചെയ്യുന്നതില് സഹായിക്കുന്നവ.

ഉദാഹരണത്തിന്: കോഴ്‌സ് കാറ്റലോഗിൽ ഏറെ മെറ്റാഡേറ്റ (നാമം, വിവരണം, നിലവാരം, ടാഗുകൾ, അധ്യാപകൻ എന്നിവ) ഉള്ളപ്പോൾ:

- "ഫാൾ 2023 കോഴ്‌സ് കാറ്റലോഗ് സംഗ്രഹിക്കുക" എന്ന നിർദ്ദേശം നിർവചിക്കാം
- പ്രാഥമിക ഉള്ളടക്കമായി വേണ്ട ഔട്ട്പുട്ട് ചില ഉദാഹരണങ്ങൾ നൽകാം
- രണ്ടാംസ്റ്റെപ്പ് ഉള്ളടക്കത്തിൽ മികച്ച 5 "ടാഗുകൾ" തിരിച്ചറിയാം

ഇപ്പോൾ, മോഡൽ ഞങ്ങൾ നൽകിയ ഉദാഹരണ രീതിയിൽ ഒരു സംഗ്രഹം നൽകും, ഒരു ഫലം നിരവധി ടാഗുകൾ ഉള്ള പക്ഷം രണ്ടാംസ്റ്റെപ്പ് ഉള്ളടക്കത്തിൽ തിരിച്ചറിഞ്ഞ 5 ടാഗുകൾ മുൻഗണന നൽകും.

---

<!--
പാഠം ടെംപ്ലേറ്റ്:
ഈ യൂണിറ്റ് കോർ ആശയം #1 ഉൾക്കൊള്ളണം.
ഉദാഹരണങ്ങളുമായി ആശയം ശക്തിപ്പെടുത്തുക.

ആശയം #3:
പ്രോംപ്റ്റ് എൻജിനീയറിംഗ് സാങ്കേതികങ്ങൾ.
പ്രാരംഭ സാങ്കേതികങ്ങളൊക്കെ എന്തൊക്കെ?
ഉദാഹരണങ്ങളോടെ വ്യക്തമാക്കുക.
-->

## പ്രോംപ്റ്റിംഗ് മികച്ച രീതികൾ

ഇപ്പോൾ, നമുക്ക് പ്രോംപ്റ്റുകൾ എങ്ങനെ _കെട്ടിപ്പടുക്കാം_ എന്നത് അറിഞ്ഞതിനുശേഷം, അവയെ _ഡിസൈൻ_ ചെയ്യാൻ കഴിവുള്ളതാ ആക്കി മെച്ചമായ പ്രവർത്തന ശീലങ്ങൾ പ്രയോഗിക്കാം. ഇത് രണ്ടായി നോക്കാം - ശരിയായ _മനോഭാവം_ ആവശ്യമാണ്, ശരിയായ _സാങ്കേതികങ്ങൾ_ പ്രയോഗിക്കുക.

### പ്രോംപ്റ്റ് എൻജിനീയറിംഗ് മനോഭാവം

പ്രോംപ്റ്റ് എൻജിനീയറിംഗ് ഒരു പരീക്ഷണത്തിലൂടെ പഠിക്കുന്ന പ്രക്രിയ ആകുന്നു; മൂന്ന് പ്രധാന മാർഗ്ഗനിർദ്ദേശങ്ങൾ തുടർച്ചയായി വായിക്കാൻ:

1. **ഡൊമെയ്ൻ അറിവ് പ്രധാനമാണ്.** പ്രതികരണത്തിന്റെ കൃത്യതയും പ്രസക്തിയുമാണ് ആ ആപ്ലിക്കേഷൻ അല്ലെങ്കിൽ ഉപഭോക്താവ് പ്രവർത്തിക്കുന്ന _ഡൊമെയ്ൻ_ എന്നിവയുടെ ഫലം. ശൈലി അനുസരിച്ചു സാങ്കേതികങ്ങൾ കൂടുതൽ തകരാറിലേക്ക് ഇട്ടുപയോഗിക്കുക. ഉദാ: സിസ്റ്റം പ്രോംപ്റ്റുകളിൽ _ഡൊമെയ്ൻ-നിർദിഷ്ട വ്യക്തിത്വങ്ങൾ_ നിർവചിക്കുക, അല്ലെങ്കിൽ ഉപയോക്തൃ പ്രോംപ്റ്റുകളിൽ _ഡൊമെയ്ൻ-സവിശേഷ ടെംപ്ലേറ്റുകൾ_ ഉപയോഗിക്കുക. രണ്ടാംസ്റ്റെപ്പ് ഉള്ളടക്കം ഡൊമെയ്ൻ കർപ്റ്റായ കേസ് നൽകുക, അല്ലെങ്കിൽ മോഡലിനെ പരിചിതമായ രീതികൾക്കായി _ഡൊമെയ്ൻ-സവിശേഷ സൂചനകളും ഉദാഹരണങ്ങളും_ ഉപയോഗിക്കുക.

2. **മോഡൽ വിശകലനം പ്രധാനമാണ്.** മോഡലുകൾ സ്വഭാവപരമായി സുഷിരമായിരിക്കും എന്ന് നാം അറിയാം. പക്ഷെ നിർവഹണങ്ങൾ വ്യത്യസ്തമായ പരിശീലന ഡാറ്റാസെറ്റുകൾ (മുൻപരിചിത അറിവ്), ലഭിക്കുന്ന ശേഷികൾ (API അല്ലെങ്കിൽ SDK വഴി) തുടങ്ങിയവ കൊണ്ടും വ്യത്യാസപ്പെടാം. നിങ്ങളുടെ മോഡലിന്റെ കഴിവുകളും കമിയുകളും മനസ്സിലാക്കി, അവയാണ് അടിസ്ഥാനമാക്കി _ജോലികൾ മുൻഗണന നൽകുകയും_, മോഡലിന്റെ ശേഷികൾക്കായി _ഏറ്റവും അനുയോജ്യമായ ടെംപ്ലേറ്റുകൾ_ രൂപപ്പെടുത്തുകയും ചെയ്യുക.

3. **പുനരാവർത്തനം & പരിശോധന പ്രധാനമാണ്.** മോഡലുകൾ വേഗത്തിൽ മാറിയിരിക്കുന്നു, പ്രോംപ്റ്റ് എൻജിനീയറിംഗ് സാങ്കേതികങ്ങളും അതുപോലെ തന്നെയാണ്. ഒരു വിദഗ്ധനെന്ന നിലയിൽ, നിങ്ങളുടെ പ്രത്യേക ആപ്ലിക്കേഷനിൽ ബാധകമായ മറ്റ് പൊതു സമൂഹത്തിന് ബാധകമല്ലാത്ത ആശയങ്ങളും മാനദണ്ഡങ്ങളും ഉണ്ടാകാം. പ്രോംപ്റ്റ് എൻജിനീയറിംഗ് ഉപകരണങ്ങളും സാങ്കേതികങ്ങളും ഉപയോഗിച്ച് നിർദ്ദേശ നിർമ്മാണം "ജമ്പ് സ്റ്റാർട്ട്" ചെയ്ത്, പിന്നെ നിങ്ങളുടെ ഇന്റ്യൂഷനും മേഖലയിലെ അറിവും ഉപയോഗിച്ച് പുനരാവർത്തിക്കുകയും പരിശോധന നടത്തുകയും ചെയ്യുക. നിങ്ങളുടെ മനസ്സിലാക്കലുകൾ രേഖപ്പെടുത്തുകയും, മറ്റുള്ളവർ വേഗം പുനരാവർത്തനം നടത്താൻ ഉപയോഗിക്കുന്ന ഒരു **അറിവ് അടിസ്ഥാനശേഖരം** (ഉദാ: പ്രോംപ്റ്റ് ലൈബ്രറികൾ) സൃഷ്ടിക്കുകയും ചെയ്യുക.

## മികച്ച പ്രാക്ടീസുകൾ

ഇവിടെ, [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) ഉം [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) പ്രാക്ടീഷനർമാർ ഉദ്ദേശിക്കുന്ന ചില സാധാരണ മികച്ച പ്രവർത്തന രീതി പറയും.

| എന്ത്                              | എന്തിനാണ്                                                                                                                                                                                                                                         |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ഏറ്റവും പുതിയ മോഡലുകൾ വിലയിരുത്തുക.       | പുതിയ മോഡൽ തലങ്ങൾ മെച്ചപ്പെട്ട ഫീച്ചറുകളും ഗുണമേൻമയുമായി വരാം - പക്ഷെ ചെലവുകൾ കൂടാം. ഫലങ്ങൾ വിലയിരുത്തി മാറാനുള്ള തീരുമാനം എടുക്കുക.                                                                                          |
| നിർദ്ദേശങ്ങളും കോൺടെക്സ്റ്റും വേർതിരിച്ച് കാട്ടുക    | നിങ്ങൾ ഉപയോഗിക്കുന്ന മോഡലും സർവീസും നിർദ്ദേശങ്ങൾ, പ്രധാന-മറ്റു ഉള്ളടക്കങ്ങൾ ദൃശ്യമായ വ്യത്യാസം നൽകുന്ന _ഡെലിമിറ്ററുകൾ_ നിർവചിക്കുന്നുവോ പരിശോധിക്കുക. ഇത് ടോക്കണുകളോടുള്ള മോഡൽ വെയ്റ്റിംഗ് കൂടുതൽ കൃത്യമായി നിഷ്ക്കർഷിക്കാൻ സഹായിക്കും.                                  |
| വ്യക്തവും വ്യക്തമായതുമാകുക               | ആവശ്യമായ കോൺടെക്സ്റ്റ്, ഫലം, നീളം, ഫോർമാറ്റ്, ശൈലി എന്നിവയെ കുറിച്ച് കൂടുതൽ വിശദാംശങ്ങൾ നൽകുക. ഫലങ്ങളുടെ ഗുണമേൻമയും സ്ഥിരതയും മെച്ചപ്പെടുത്തും. ആവർപ്പാപിക്കാവുന്ന ടെംപ്ലേറ്റുകളിൽ സൂത്രവാക്യം കൈപ്പിടുക്കുക.                                                                   |
| വിവരണാത്മകവും ഉദാഹരണവുമായി ഉപയോഗിക്കുക      | മോഡലുകൾ "കാണിച്ച് പറഞ്ഞാൽ" മെച്ചപ്പെട്ട പ്രതികരണം നൽകാം. ആദ്യം `സീറോ-ഷോട്ട്` രീതിയിൽ ഒരു നിർദ്ദേശം നൽകുക (എന്തുമില്ലാതെ ഉദാഹരണങ്ങൾ ഇല്ലാതെ), പിന്നെ ബാഗായി ചില output ഉദാഹരണങ്ങൾ നൽകി `ഫ്യൂ-ഷോട്ട്` ചെറുതായി മെച്ചപ്പെടുത്തുക. ഉപമകൾ വരെ ഉപയോഗിക്കാം.                   |
| ജംപ്പ് സ്റ്റാർട്ട് ചെയ്യുന്നതിന് സൂചനകൾ ഉപയോഗിക്കുക | വിവരണത്തിന്റെ തുടക്കത്തിൽ പ്രാരംഭ വാക്കുകൾ അല്ലെങ്കിൽ വാക്യങ്ങൾ നൽകുക, ഇതിനെ വഴിവഴിച്ചു നിയന്ത്രിച്ച തീർച്ചയായ ഫലത്തിലേക്ക് നയിക്കാൻ സഹായിക്കും.                                                                                                  |
| ആവർത്തിക്കുക                       | ചിലപ്പോൾ മോഡലിന് നീക്കം ചെയ്യേണ്ടതുണ്ടാവാം. നിർദ്ദേശങ്ങൾ പ്രാഥമികവും അവസാനവുമായുള്ള ഭാഗങ്ങളിൽ നല്‍കുക, നിർദ്ദേശവും സൂചനയും എന്നിവ ഉപയോഗിക്കുക. പുനരാവർത്തിച്ച് ഫലങ്ങൾ പരിശോധിച്ച് നേരത്തെയുള്ളവയേക്കാൾ മെച്ചമാണ് എന്ന് കണ്ടെത്തുക.                                                                    |
| ക്രമീകരണം പ്രധാനമാണ്               | നിങ്ങൾ മോഡലിനോട് വെളിപ്പെടുത്തുന്ന വിവരങ്ങളുടെ ക്രമീകരണം ഫലത്തെ ബാധിക്കാം, പ്രത്യേകിച്ച് പഠന ഉദാഹരണങ്ങളിൽ അത്യംശിക താൽപര്യത്തിൽ (recency bias) കാരണം. വ്യത്യസ്ത ഓപ്ഷനുകൾ പരീക്ഷിച്ച് മികച്ചത് കണ്ടെത്തുക.                                                                                |
| മോഡലിന് “അവസാന സാധ്യത” നൽകുക           | മോഡലിന് ഒരു _ബാക്കപ്പ്_ പൂർത്തിയാക്കാനുള്ള ഓപ്ഷൻ നൽകുക, വൃത്തിഹീനമായ അല്ലെങ്കിൽ കൃത്യം രണ്ടാം വ്യത്യസ്തമായ ഫലങ്ങൾ ഉണ്ടാകാതിരിക്കാൻ.                                                                                                                      |
|                                   |                                                                                                                                                                                                                                                   |

ഏതൊരു മികച്ച പ്രവൃത്തിയെന്ന നിലയിൽ, മോഡലിന്റെ, ജോലിയുടെ, ഡൊമെയ്‌നിന്റെ അടിസ്ഥാനത്തിൽ _നിങ്ങളുടെ അനുഭവം വ്യത്യാസപ്പെട്ടേക്കാം_. ഇതിനെ ஆரம்பബിന്ദുവായി ഉപയോഗിച്ച്, നിങ്ങളുടെ ആവശ്യാനുസരണത്തിനായി പുനരാവർത്തിച്ച് മെച്ചപ്പെട്ട രീതികൾ കണ്ടെത്തുക. പുതിയ മോഡലുകളും സാദ്ധ്യമായ ഉപകരണങ്ങളും ലഭ്യമാകുമ്പോൾ, പ്രോംപ്റ്റ് എൻജിനീയറിംഗ് പ്രക്രിയ വീണ്ടും വിലയിരുത്തുന്നതിലുള്ള ശ്രദ്ധ കൂടിക്കുക—പ്രക്രിയയുടെ വിപുലീകരണവും പ്രതികരണ ഗുണമേന്മയുമാണ് പ്രധാനപരിഗണന.

<!--
പാഠം ടെംപ്ലേറ്റ്:
ഈ യൂണിറ്റ് ആവശ്യമായ പക്ഷം ഒരു കോഡ് വെല്ലുവിളി നൽകണം.

വെല്ലുവിളി:
ഒരു Jupyter നോട്ട്‌ബുക്കിന്റെ ലിങ്ക്, നിർദ്ദേശങ്ങളിൽ മാത്രം കോഡ് കമെന്റുകൾ ഉള്ള (കോഡ് സെക്ഷനുകൾ ശൂന്യമാണ്).

പരിഹാരം:
അതിനുള്ള നോട്ട്‌ബുക്കിന്റെ ഒരു പകർപ്പ്, പ്രോംപ്റ്റ് നിറച്ചും പ്രവർത്തിപ്പിച്ചും, ഒരു ഉദാഹരണ ഫലം കാണിക്കുന്നതും.
-->

## അസൈൻമെന്റ്

അഭിനന്ദനങ്ങൾ! പാഠത്തിന്റെ അവസാനത്തിലേക്ക് എത്തിയിരിക്കുന്നു! ഇപ്പോൾ ആ ആശയങ്ങളും സാങ്കേതിക വിദ്യകളും യാഥാർത്ഥ്യത്തിൽ പരീക്ഷിക്കാൻ സമയം.

നമ്മുടെ അസൈൻമെന്റിനായി, നിങ്ങൾക്ക് ഇടപെടാവുന്ന ഒരു Jupyter നോട്ട്‌ബുക്ക് ഉപയോഗിക്കും. നിങ്ങളുടെ സ്വന്തം മാർക്ക്ഡൗൺ, കോഡ് സെല്ലുകളും ചേർത്ത് ആശയങ്ങൾ സ്വതന്ത്രമായി പരീക്ഷിക്കാം.

### തുടക്കം കുറിക്കാൻ, റീപ്പോയെ ഫോർക്ക് ചെയ്യുക, പിന്നെ

- (ശിപാർശചെയ്യുന്നു) GitHub Codespaces ആരംഭിക്കുക
- (മറ്റൊരു ഉപാധി) റീപ്പോ നിങ്ങളുടെ പ്രാദേശിക ഉപകരണത്തിൽ ക്ലോൺ ചെയ്ത് Docker Desktop ഉപയോഗിക്കുക
- (മറ്റൊരു പരിഹാരം) നിങ്ങളുടെ ഇഷ്ട പ്രകൃതിയുടെ നോട്ട്‌ബുക്ക് റൺടൈം ഉപയോഗിച്ച് നോട്ട്‌ബുക്ക് തുറക്കുക.

### തുടർന്ന്, உங்கள் പരിസ്ഥിതിvariableകൾ ക്രമീകരിക്കുക

- റീപ്പോ റൂട്ട് ഡിറക്ടറിയിലുള്ള `.env.copy` ഫയൽ `.env` ആയി പകർത്തുക, `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT` മൂല്യങ്ങൾ രേഖപ്പെടുത്തുക. [Learning Sandbox വിഭാഗം](#പഠന-സാമ്പ്‌ബോക്സ്) കാണുക.

### പിന്നെ, Jupyter നോട്ട്‌ബുക്ക് തുറക്കുക

- റൺടൈം കർണൽ തിരഞ്ഞെടുക്കുക. നിങ്ങൾ ഓപ്ഷൻ 1 അല്ലെങ്കിൽ 2 ഉപയോഗിക്കുന്നെങ്കിൽ, ഡെവ് കണ്ടെയ്നറിൽ ഡിഫോൾട്ട് ആയി ലഭിക്കുന്ന Python 3.10.x കർണൽ തിരഞ്ഞെടുക്കുക.

നിങ്ങൾ ശ്രമങ്ങൾ നടത്താൻ സജ്ജമാണ്. ഇത് _തെറ്റും ശരിയും_ ഉണ്ട് എന്ന ആശയം ഇല്ല - പരീക്ഷണത്തിലൂടെ തിരഞ്ഞെടുക്കലും മൊഡലിനുള്ള പരിജ്ഞാനവുമാണ് സുപ്രധാനമെന്ന് മനസ്സിലാക്കുക.

_ഇതിനാൽ ഈ പാഠത്തിൽ പ്രത്യേകമായി കോഡ് പരിഹാര സെക്ഷനുകൾ ഇല്ല. പകരം, നോട്ട്‌ബുക്കിൽ "എന്റെ പരിഹാരം:" എന്നമതിലെ മാർക്ക്ഡൗൺ സെലുകൾ ഒപ്പം ഒരു ഉദാഹരണ output കാണിക്കും._

 <!--
പാഠം ടെംപ്ലേറ്റ്:
ഈ ഭാഗം സ്വയം അധ്യാപനത്തിനായി സംഗ്രഹവും റിസോഴ്‌സുകളും സഹിതം അടയ്ക്കുക.
-->

## അറിവ് പരിശോധിക്കൽ

താഴെ ഉള്ളവയിൽ ഏതാണ് ശരിയായ നൂതനപ്രോംപ്റ്റിൽ നിന്നും സ്വീകരിക്കാവുന്നതുള്ള ഒരു നല്ല പ്രോംപ്റ്റ്?

1. ഒരു ചുവന്ന കാർ ചിത്രമൂം കാണിക്കൂ
2. വോൾവോ തയാറാക്കിയ XC90 മോഡലിന്റെ ചുവന്ന കാർ, ഒരു മറിയുന്ന വഴി அருகിൽ സൂര്യാസ്തമയത്തോടെ നിർത്തിയത് എന്ന ഒരു ചിത്രം കാണിക്കൂ
3. വോൾവോ തയാറാക്കിയ XC90 മോഡലിന്റെ ചുവന്ന കാർ കാണിക്കൂ

ഉത്തരം: 2, ഇത് ഏറ്റവും നല്ല പ്രോംപ്റ്റാണ് കാരണം "എന്ത്" എന്നതും വിശദമായി പറയുകയും (സാധാരണ ഏത് കാർ അല്ല, ഒരു സ്പെസിഫിക് തയാറാക്കൽ, മോഡൽ) മൊത്തം പശ്ചാത്തലവും വിവരിക്കുന്നു. 3 അടുത്ത ഏറ്റവും നല്ലതാണ് കാരണം അതിലും സാധുവായ വിവരണം കൂടുതലാണ്.

## 🚀 വെല്ലുവിളി

"cue" സാങ്കേതികം പ്രയോജനപ്പെടുത്തി ഈ പ്രോംപ്റ്റ് പരീക്ഷിക്കുക: "Show me an image of red car of make Volvo and ". അത് എന്താണ് പ്രതികരിക്കുന്നത്? നിങ്ങൾ അത് എങ്ങനെ മെച്ചപ്പെടുത്തുമെന്നു കാണിക്കുക.

## നല്ല ജോലി! നിങ്ങളുടെ പഠനം തുടരുമോ?

വിവിധ പ്രോംപ്റ്റ് എൻജിനീയറിംഗ് ആശയങ്ങൾക്കുറിച്ച് കൂടുതൽ അറിയാനാണോ? ഈ [തുടരുന്ന പഠന പേജ്](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) സന്ദർശിച്ച് ഇതുമായി ബന്ധപ്പെട്ട മറ്റ് കാഴ്ചപ്പാടുകളും വൃത്താന്തങ്ങളും നേടുക.

പാഠം 5-ൽ നൂതന [അഡ്വാൻസ്ഡ് പ്രോംപ്റ്റിംഗ് സാങ്കേതികതകൾ](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst) കാണാം!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:
ഈ രേഖ AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള അസൽ രേഖയാണ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾ അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കായി ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->