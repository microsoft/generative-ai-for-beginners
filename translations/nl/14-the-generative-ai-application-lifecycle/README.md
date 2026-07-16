[![Integratie met functie-aanroepen](../../../translated_images/nl/14-lesson-banner.066d74a31727ac12.webp)](https://youtu.be/ewtQY_RJrzs?si=dyJ2bjiljH7UUHCh)

# De levenscyclus van generatieve AI-toepassingen

Een belangrijke vraag voor alle AI-toepassingen is de relevantie van AI-functies, aangezien AI een snel evoluerend vakgebied is. Om ervoor te zorgen dat jouw toepassing relevant, betrouwbaar en robuust blijft, moet je deze continu monitoren, evalueren en verbeteren. Dit is waar de levenscyclus van generatieve AI om de hoek komt kijken.

De levenscyclus van generatieve AI is een raamwerk dat je begeleidt bij de fasen van het ontwikkelen, implementeren en onderhouden van een generatieve AI-toepassing. Het helpt je je doelen te definiëren, je prestaties te meten, je uitdagingen te identificeren en je oplossingen te implementeren. Het helpt je ook om je toepassing af te stemmen op de ethische en juridische normen van je domein en je belanghebbenden. Door de levenscyclus van generatieve AI te volgen, kun je ervoor zorgen dat je toepassing altijd waarde levert en je gebruikers tevredenstelt.

## Introductie

In dit hoofdstuk zul je:

- Het paradigma-verandering van MLOps naar LLMOps begrijpen
- De levenscyclus van LLM
- Tools voor de levenscyclus
- Metrificatie en evaluatie in de levenscyclus

## Het paradigma-verandering van MLOps naar LLMOps begrijpen

LLM’s zijn een nieuw instrument in het arsenaal van kunstmatige intelligentie, ze zijn ongelooflijk krachtig in analyse- en generatietaken voor toepassingen, echter heeft deze kracht ook gevolgen voor hoe we AI en klassieke machine learning taken stroomlijnen.

Hiervoor hebben we een nieuw paradigma nodig om dit instrument op een dynamische manier aan te passen, met de juiste stimulansen. We kunnen oudere AI-apps categoriseren als "ML Apps" en nieuwere AI-apps als "GenAI Apps" of gewoon "AI Apps", reflecterend de mainstream technologie en technieken die toen gebruikt werden. Dit verandert ons verhaal op meerdere manieren, bekijk de volgende vergelijking.

![LLMOps versus MLOps vergelijking](../../../translated_images/nl/01-llmops-shift.29bc933cb3bb0080.webp)

Merk op dat we bij LLMOps meer gericht zijn op de app-ontwikkelaars, waarbij integraties een belangrijk punt zijn, gebruikmakend van "Models-as-a-Service" en nadenken over de volgende punten voor metrics.

- Kwaliteit: Antwoordkwaliteit
- Schade: Verantwoorde AI
- Eerlijkheid: Grondslag van het antwoord (Maakt het zin? Is het correct?)
- Kosten: Oplossingsbudget
- Latentie: Gemiddelde tijd voor token reactie

## De levenscyclus van de LLM

Om eerst de levenscyclus en de wijzigingen te begrijpen, laten we naar de volgende infographic kijken.

![LLMOps infographic](../../../translated_images/nl/02-llmops.70a942ead05a7645.webp)

Zoals je misschien ziet, is dit anders dan de gebruikelijke levenscycli van MLOps. LLM’s hebben veel nieuwe vereisten, zoals Prompting, verschillende technieken om kwaliteit te verbeteren (Fine-Tuning, RAG, Meta-Prompts), een andere beoordeling en verantwoordelijkheid met verantwoorde AI, en ten slotte nieuwe evaluatiemetrics (Kwaliteit, Schade, Eerlijkheid, Kosten en Latentie).

Neem bijvoorbeeld eens een kijkje hoe we ideeën vormen. We gebruiken prompt engineering om met verschillende LLM’s te experimenteren om mogelijkheden te exploreren en te testen of hun hypothese correct kan zijn.

Merk op dat dit niet lineair is, maar geïntegreerde loops, iteratief en met een overkoepelende cyclus.

Hoe kunnen we die stappen verkennen? Laten we in detail stappen hoe we een levenscyclus kunnen bouwen.

![LLMOps Workflow](../../../translated_images/nl/03-llm-stage-flows.3a1e1c401235a6cf.webp)

Dit ziet er misschien wat ingewikkeld uit, laten we eerst focussen op de drie grote stappen.

1. Ideeën vormen/Verkennen: Exploratie, hier kunnen we verkennen volgens onze zakelijke behoeften. Prototyping, het creëren van een [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) en testen of het efficiënt genoeg is voor onze hypothese.
1. Bouwen/Versterken: Implementatie, nu beginnen we te evalueren voor grotere datasets en implementeren technieken zoals Fine-tuning en RAG, om de robuustheid van onze oplossing te controleren. Als het niet werkt, kan herimplementatie, toevoegen van nieuwe stappen in onze flow of herstructureren van de data helpen. Na het testen van onze flow en schaal, als het werkt en onze metrics checken, is het klaar voor de volgende stap.
1. Operationeel maken: Integratie, nu toevoegen van monitorings- en waarschuwingssystemen aan ons systeem, implementatie en applicatie-integratie met onze toepassing.

Vervolgens hebben we de overkoepelende cyclus van beheer, met focus op beveiliging, compliance en governance.

Gefeliciteerd, je hebt nu je AI-app klaar voor gebruik en operationeel. Voor een praktijkervaring, neem een kijkje bij de [Contoso Chat Demo.](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst)

Nu, welke tools kunnen we gebruiken?

## Tools voor de levenscyclus

Voor tools biedt Microsoft het [Azure AI Platform](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreyst) en [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) die je cyclus vergemakkelijken en gemakkelijk te implementeren maken.

Het [Azure AI Platform](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreyst) laat je gebruikmaken van [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst). Microsoft Foundry (voorheen Azure AI Studio) is een webportaal waarmee je modellen, voorbeelden en tools kunt ontdekken, je resources kunt beheren, en UI-ontwikkelingsflows kunt gebruiken evenals SDK/CLI-opties voor code-first ontwikkeling.

![Mogelijkheden van Azure AI](../../../translated_images/nl/04-azure-ai-platform.80203baf03a12fa8.webp)

Azure AI laat je meerdere resources gebruiken om je operaties, services, projecten, vectorzoekopdrachten en databasebehoeften te beheren.

![LLMOps met Azure AI](../../../translated_images/nl/05-llm-azure-ai-prompt.a5ce85cdbb494bdf.webp)

Bouwen, van proof-of-concept (POC) tot grootschalige toepassingen met PromptFlow:

- Ontwerp en bouw apps vanuit VS Code, met visuele en functionele tools
- Test en fine-tune je apps voor kwaliteitsvolle AI, eenvoudig.
- Gebruik Microsoft Foundry om te integreren en itereren met de cloud, Push en Deploy voor snelle integratie.

![LLMOps met PromptFlow](../../../translated_images/nl/06-llm-promptflow.a183eba07a3a7fdf.webp)

## Geweldig! Ga door met leren!

Fantastisch, leer nu meer over hoe we een toepassing structureren om de concepten te gebruiken met de [Contoso Chat App](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst), om te zien hoe Cloud Advocacy die concepten toevoegt in demonstraties. Voor meer content, bekijk onze [Ignite breakout sessie!
](https://www.youtube.com/watch?v=DdOylyrTOWg)

Bekijk nu les 15 om te begrijpen hoe [Retrieval Augmented Generation en Vector Databases](../15-rag-and-vector-databases/README.md?WT.mc_id=academic-105485-koreyst) Generative AI beïnvloeden en hoe je meer boeiende toepassingen maakt!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->