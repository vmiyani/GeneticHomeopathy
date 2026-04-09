import os
import re

# Data structure for all 9 treatment categories
categories = [
    {
        "id": "skin",
        "filename": "treatment-skin.html",
        "title": "Skin Diseases",
        "title_lower": "skin",
        "image": "assets/images/treat-skin-bg.png",
        "subtitle": "Clear, radiantly healthy skin achieved by treating constitutional imbalances through holistic internal healing.",
        "intro_html": "<p>Dr. Riddhi Mayani treats skin conditions through a holistic approach. Homeopathy believes that the skin is a mirror of internal health and true resolution comes from within.</p><p>By understanding your entire medical history, stress levels, immunity, and genetics, we prescribe gentle, individualized remedies that aim to resolve the root disturbance. This approach offers safe, long-lasting relief from persistent skin disorders by supporting the body's natural restorative power.</p>",
        "what_is_html": "<p>Skin diseases involve acute or chronic inflammation of the epidermis and dermis. They can present as rashes, flaking, redness, severe itching, fluid-filled blisters, or scaling.</p><p>While they appear externally, these manifestations are typically an outward expression of an internal imbalance—such as an overactive immune system, hormonal fluctuations, digestive toxicity, or emotional stress.</p>",
        "symptoms": [
            "Persistent itching, redness, or inflammation",
            "Dry, scaling, or flaking skin plaques",
            "Weeping or fluid-filled blisters and eruptions",
            "Painful cysts, nodules, or severe acne breakouts",
            "Discoloration, hyperpigmentation, or loss of pigment"
        ],
        "causes": [
            "Immune system hypersensitivity and allergic reactions",
            "Underlying hormonal imbalances and fluctuations",
            "Digestive dysfunction or poor gut health (microbiome imbalance)",
            "Systemic stress, anxiety, or emotional trauma",
            "Genetic predispositions and family history"
        ],
        "tips": [
            {"title": "Hydrate Well", "text": "Drink plenty of water to maintain skin elasticity and assist in toxin elimination."},
            {"title": "Natural Cleansing", "text": "Use mild, fragrance-free natural cleansers to avoid stripping the skin of its protective oils."},
            {"title": "Breathable Fabrics", "text": "Wear cotton or natural fibers to minimize skin irritation and allow the skin to breathe."},
            {"title": "Stress Management", "text": "Practice relaxation techniques as stress is a major trigger for many skin flares."}
        ],
        "faqs": [
            {"q": "Is homeopathy safe for babies with eczema?", "a": "Yes, homeopathic remedies are exceptionally gentle, non-invasive, and safe for infants and children of all ages."},
            {"q": "How long does it take to see results in skin conditions?", "a": "Chronic skin issues vary, but many patients notice improvement in itching and inflammation within a few weeks of consistent treatment."},
            {"q": "Can homeopathy treat severe acne?", "a": "Yes, homeopathy addresses the hormonal and digestive imbalances that often trigger severe or cystic acne."}
        ]
    },
    {
        "id": "respiratory",
        "filename": "treatment-respiratory.html",
        "title": "Respiratory Conditions",
        "title_lower": "respiratory",
        "image": "assets/images/hero-slide-1.png", # using existing high quality slide as placeholder
        "subtitle": "Breathe easier with natural, non-habit-forming homeopathic care that strengthens your respiratory system's immunity.",
        "intro_html": "<p>Respiratory issues, whether acute like the seasonal flu or chronic like asthma, can severely impact your quality of life. Dr. Riddhi Mayani utilizes highly customized homeopathic formulations to naturally support the respiratory tract's resilience.</p><p>Our treatments focus on building respiratory strength and boosting your immune system’s natural defenses against allergens, pollutants, and weather changes, promoting lasting wellness and easier breathing.</p>",
        "what_is_html": "<p>Respiratory conditions encompass disorders affecting the lungs, airways, sinuses, and nasal passages. They involve the inflammation or obstruction of the respiratory tract, making breathing difficult, painful, or uncomfortable.</p><p>These conditions range from allergic rhinitis (hay fever) and chronic sinusitis to deeper issues like bronchitis and asthma. They are predominantly related to the body's response to environmental triggers.</p>",
        "symptoms": [
            "Chronic cough, wheezing, or shortness of breath",
            "Frequent sneezing, runny nose, and nasal congestion",
            "Pressure, pain, or heaviness in the facial sinuses",
            "Tightness in the chest or restricted breathing",
            "Recurrent throat infections or constantly swollen tonsils"
        ],
        "causes": [
            "Hypersensitivity to environmental allergens (pollen, dust, pet dander)",
            "Poor systemic immunity leading to recurrent infections",
            "Exposure to harsh airborne pollutants or chemicals",
            "Unresolved childhood respiratory illnesses",
            "Genetic predisposition to asthma or atopy"
        ],
        "tips": [
            {"title": "Clean Air", "text": "Keep your living space well-ventilated and consider a HEPA air purifier to reduce allergens."},
            {"title": "Deep Breathing", "text": "Practice regular pranayama or deep breathing exercises to improve lung capacity."},
            {"title": "Steam Inhalation", "text": "Use plain steam to soothe irritated airways and clear nasal passages naturally."},
            {"title": "Stay Active", "text": "Moderate exercise helps strengthen the respiratory muscles and improves oxygenation."}
        ],
        "faqs": [
            {"q": "Can homeopathy help with chronic asthma?", "a": "Homeopathy works to reduce the frequency and intensity of asthma attacks by strengthening the respiratory immune response."},
            {"q": "Are the remedies non-drowsy?", "a": "Yes, unlike standard antihistamines, homeopathic remedies are completely non-drowsy and do not interfere with daily activities."},
            {"q": "How does it help with seasonal hay fever?", "a": "Remedies are tailored to your specific symptoms—whether it's watery eyes or sneezing—to help the body desensitize naturally."}
        ]
    },
    {
        "id": "digestive",
        "filename": "treatment-digestive.html",
        "title": "Digestive Disorders",
        "title_lower": "digestive",
        "image": "assets/images/treat-digestive-bg.png", # I'll assume this may exist or use a slide
        "subtitle": "Restore gut health and digestive harmony with individualized remedies that address underlying gastrointestinal function.",
        "intro_html": "<p>The digestive system is the core of our overall health. The homeopathic approach to digestive disorders focuses heavily on the gut-brain axis and your constitutional makeup. Dr. Riddhi Mayani thoroughly investigates not just diet, but how your body processes stress and emotions.</p><p>By treating the individual, our homeopathic remedies soothe gut linings, support enzymatic function, and promote lasting rhythmic bowel harmony by restoring the body's natural digestive rhythm.</p>",
        "what_is_html": "<p>Digestive disorders refer to a wide spectrum of health issues occurring anywhere in the gastrointestinal (GI) tract, from the esophagus and stomach to the intestines and liver.</p><p>Conditions such as Irritable Bowel Syndrome (IBS), Acid Reflux (GERD), and Ulcerative Colitis are increasingly common. They disrupt the body’s ability to digest food, absorb vital nutrients, and successfully eliminate waste.</p>",
        "symptoms": [
            "Chronic abdominal pain, cramping, or severe bloating",
            "Frequent acid reflux, heartburn, or severe indigestion",
            "Persistent constipation, diarrhea, or irregular bowel movements",
            "Unexplained nausea, vomiting, or loss of appetite",
            "Presence of mucus or blood in the stool"
        ],
        "causes": [
            "Prolonged chronic stress and nervous system dysregulation",
            "Poor dietary habits, nutritional deficiencies, and food intolerances",
            "Systemic imbalances impact gut health",
            "Sedentary lifestyle and lack of adequate hydration",
            "Underlying inflammatory markers in the GI system"
        ],
        "tips": [
            {"title": "Mindful Eating", "text": "Chew your food thoroughly and eat in a calm, relaxed environment to aid digestion."},
            {"title": "Hydration", "text": "Drink adequate water throughout the day, but avoid excess fluids during meals."},
            {"title": "Fiber Balance", "text": "Maintain a diet rich in natural fiber from vegetables and whole grains for bowel health."},
            {"title": "Regular Intervals", "text": "Try to eat meals at fixed times every day to help regulate your digestive system."}
        ],
        "faqs": [
            {"q": "Can homeopathy treat Irritable Bowel Syndrome (IBS)?", "a": "Yes, homeopathy is very effective for IBS as it addresses the emotional and physiological triggers of the condition."},
            {"q": "Will I become dependent on the remedies?", "a": "No, homeopathic remedies are designed to stimulate the body's own healing, not create a dependency."},
            {"q": "Can it help with chronic acid reflux?", "a": "Homeopathy addresses the root causes of excess acidity to provide long-lasting relief rather than just temporary relief."}
        ]
    },
    {
        "id": "mental",
        "filename": "treatment-mental.html",
        "title": "Mental & Emotional Health",
        "title_lower": "mental and emotional",
        "image": "assets/images/treat-mental-bg.png",
        "subtitle": "Gentle, comprehensive care for psychological well-being that promotes emotional balance and resilience.",
        "intro_html": "<p>Mental health is a vital constituent of an individual's general well-being. Dr. Riddhi Mayani takes a deeply holistic approach to mental and emotional wellness. Homeopathy recognizes the deep link between mind and body, aiming at healing the connection from its root.</p><p>Homeopathy works by evaluating your state of health, emotions, specific fears, and precise mind-frame. By utilizing natural micro-doses, it gently activates the body's intrinsic ability to balance and resolve deeper emotional blockages.</p>",
        "what_is_html": "<p>Mental diseases are conditions of the mind that fundamentally alter a person’s mood, emotional processing, cognitive thoughts, and behavior. These states can impact an individual’s ability to handle everyday tasks and maintain relationships.</p><p>Common conditions targeted by homeopathy include Generalized Anxiety, Clinical Depression, OCD, Panic Attacks, PTSD, and severe Insomnia. Homeopathic medicine offers a gentle way to address these states by supporting the body's own restorative responses.</p>",
        "symptoms": [
            "Consistent hopelessness, persistent sadness, or severe low mood",
            "Constant debilitating worry, fear, or generalized anxiety",
            "Rhythmic shifts in mood, or extreme emotional highs and lows",
            "Complete detachment from social activities and loved ones",
            "Inability to focus, extreme irritability, or chronic changes in sleep patterns"
        ],
        "causes": [
            "Prolonged exposure to extreme emotional stress or trauma",
            "Systemic imbalances in brain chemistry and hormonal shifts",
            "Deep-seated grief, sudden emotional shock, or tragic loss",
            "Undermined physical health or chronic chronic pain conditions",
            "Genetic predispositions alongside environmental triggers"
        ],
        "tips": [
            {"title": "Mindfulness", "text": "Spend at least 10 minutes daily in meditation or quiet reflection to ground your thoughts."},
            {"title": "Sleep Hygiene", "text": "Create a consistent sleep routine to help regulate your body's circadian rhythm and mood."},
            {"title": "Limit Stimulants", "text": "Reduce intake of caffeine and sugar, which can trigger anxiety and sleep disruptions."},
            {"title": "Stay Connected", "text": "Reach out to trusted friends and family; social support is vital for emotional health."}
        ],
        "faqs": [
            {"q": "Is homeopathy effective for anxiety and panic?", "a": "Yes, remedies are chosen based on your specific type of anxiety to help restore calm naturally."},
            {"q": "Are the remedies habit-forming?", "a": "No, homeopathic medicines are non-habit forming and do not cause dependency or withdrawal issues."},
            {"q": "How does it help with chronic insomnia?", "a": "By calming the nervous system and addressing underlying stress, it helps restore natural sleep patterns."}
        ]
    },
    {
        "id": "joint",
        "filename": "treatment-joint.html",
        "title": "Joint & Musculoskeletal",
        "title_lower": "joint and bone",
        "image": "assets/images/hero-slide-3.png", # existing clinic image
        "subtitle": "Manage chronic pain, stiffness, and mobility naturally through restorative homeopathic care.",
        "intro_html": "<p>Joint and musculoskeletal pain can affect your mobility and balance. At GeneticHomeopathy, Dr. Riddhi Mayani provides a profoundly gentle approach to bone and joint health centered on long-term relief and metabolic recovery.</p><p>Homeopathic therapies focus on reducing systemic inflammation, supporting joint health, and improving the mobility of the patient. Individualized remedies target precise types of pain—whether it is stiffness, aching, or burning sensations.</p>",
        "what_is_html": "<p>Joint and musculoskeletal disorders affect the bones, muscles, ligaments, tendons, and joints of the human body. These conditions can impact movement, flexibility, and comfort levels.</p><p>Ranging from age-related wear-and-tear like Osteoarthritis to systemic inflammatory responses like Gout, musculoskeletal conditions require comprehensive metabolic and lifestyle management.</p>",
        "symptoms": [
            "Deep, aching, or sharp pain in major joints (knees, hips, shoulders)",
            "Pronounced morning stiffness that restricts immediate mobility",
            "Visible swelling, redness, or heat emanating from the joint",
            "Restricted range of motion or an absolute inability to bend",
            "Numbness, tingling, or radiating nerve pain (like Sciatica)"
        ],
        "causes": [
            "Progressive wear and tear of cartilage due to age or overuse",
            "Autoimmune conditions where the body targets joint tissue",
            "Metabolic disorders leading to crystal deposition (Gout)",
            "Historical physical injuries, strains, fractures, or blunt trauma",
            "Poor posture, sedentary habits, and nutritional deficiencies"
        ],
        "tips": [
            {"title": "Stay Active", "text": "Gentle, low-impact exercises like walking or swimming keep joints flexible without strain."},
            {"title": "Anti-inflammatory Diet", "text": "Include foods rich in omega-3 and antioxidants to support joint health internally."},
            {"title": "Posture Check", "text": "Pay attention to your posture, especially if you spend long hours at a desk or computer."},
            {"title": "Maintain Weight", "text": "Keeping a healthy weight reduces the constant mechanical stress on your weight-bearing joints."}
        ],
        "faqs": [
            {"q": "Can homeopathy help with Rheumatoid Arthritis?", "a": "Homeopathy helps manage systemic inflammation and reduce the chronic pain associated with RA."},
            {"q": "Is it a good alternative to daily painkillers?", "a": "Yes, many patients transition to homeopathy to manage chronic pain without the systemic burden of daily medication."},
            {"q": "Does it improve joint flexibility?", "a": "By reducing inflammation and stiffness, remedies help restore a better range of motion naturally."}
        ]
    },
    {
        "id": "women",
        "filename": "treatment-women.html",
        "title": "Women's Health",
        "title_lower": "women's health",
        "image": "assets/images/hero-slide-2.png", # existing slide
        "subtitle": "Safe, hormone-free treatment designed specifically for female reproductive and hormonal health across every life stage.",
        "intro_html": "<p>A woman's body undergoes extraordinary, complex hormonal shifts throughout her life. Dr. Riddhi Mayani provides deeply empathetic and specialized care utilizing purely natural homeopathic medicines that gently support the endocrine system.</p><p>Our holistic treatments work in harmony with the female body to balance hormones naturally, respecting the intricate rhythm of each individual to restore true well-being and vitality.</p>",
        "what_is_html": "<p>Women's health conditions refer broadly to gynecological, reproductive, and hormonal disorders specifically affecting female anatomy and the endocrine cycle.</p><p>These cover a wide spectrum of conditions including PCOS (Polycystic Ovary Syndrome), PMS, Endometriosis, Uterine Fibroids, Menopause symptoms, and thyroid-related wellness.</p>",
        "symptoms": [
            "Extremely painful, irregular, exceptionally heavy, or absent menstrual cycles",
            "Severe pelvic pain, cramping, or generalized lower abdominal heaviness",
            "Intense hot flashes, night sweats, and aggressive mood fluctuations",
            "Unexplained weight gain, persistent acne, or disruptive facial hair growth",
            "Challenges related to natural reproductive health and hormonal balance"
        ],
        "causes": [
            "Systemic hormonal imbalances (estrogen/progesterone shifts)",
            "Thyroid gland dysfunction significantly impacting the metabolic rate",
            "High levels of physiological stress disrupting the cycle",
            "Genetic predispositions toward cysts or endometriosis",
            "Underlying nutritional deficiencies and metabolic markers"
        ],
        "tips": [
            {"title": "Cycle Tracking", "text": "Keep a regular log of your cycle and symptoms to understand your body's unique patterns."},
            {"title": "Healthy Fats", "text": "Include healthy fats like flaxseeds and avocados to support hormone production naturally."},
            {"title": "Stress Management", "text": "Since hormones are stress-sensitive, prioritize daily relaxation or yoga."},
            {"title": "Limit Sugar", "text": "Reducing refined sugar can help balance insulin levels, which is vital for PCOS and hormonal health."}
        ],
        "faqs": [
            {"q": "Can homeopathy treat PCOS naturally?", "a": "Yes, homeopathy addresses the internal hormonal pathways to help regulate cycles and manage symptoms like acne or weight gain."},
            {"q": "Is it safe during menopause?", "a": "Absolutely, it offers a gentle way to manage hot flashes, mood swings, and sleep issues without hormones."},
            {"q": "Will it help with painful periods (PMS)?", "a": "Homeopathy is highly effective at reducing the intensity of cramps and emotional PMS symptoms."}
        ]
    },
    {
        "id": "pediatric",
        "filename": "treatment-pediatric.html",
        "title": "Pediatric Care",
        "title_lower": "pediatric",
        "image": "assets/images/doctor-riddhi.png", # doctor slide
        "subtitle": "Non-toxic, exceptionally gentle remedies perfectly safe for infants and children to build a foundation of lifelong immunity.",
        "intro_html": "<p>Children require exceptionally mild yet deeply effective medical care. Dr. Riddhi Mayani specializes in homeopathic pediatric care because they are exceptionally gentle, safe for all ages, and designed to support the body's natural healing processes effectively.</p><p>Because homeopathic pills are sweet and easily dissolved, they are simple to administer even to infants. Our treatments aim not only to resolve immediate issues but to fundamentally strengthen the child's developing immune and nervous systems.</p>",
        "what_is_html": "<p>Pediatric conditions involve the broad spectrum of physical, behavioral, and developmental ailments that affect infants, toddlers, and adolescents as they rapidly grow.</p><p>These range from acute issues like recurring ear infections, teething pain, and colic, to complex developmental and behavioral challenges like ADHD or autism spectrum support.</p>",
        "symptoms": [
            "Recurrent acute fevers, constant earaches, or repetitive sore throats",
            "Severe colic, infant acid reflux, or unexplained digestive upset",
            "Noticeable hyperactivity, complete inability to focus, or extreme impulsivity",
            "Frequent bedwetting (enuresis) in older children",
            "Delayed speech, delayed walking, or disrupted physical growth"
        ],
        "causes": [
            "An immature, actively developing, or hypersensitive immune system",
            "Genetic predispositions or strong familial history of allergies",
            "Nutritional malabsorption interfering with rapid development",
            "Environmental triggers and food sensitivities",
            "Emotional sensitivities and disruptions in routines"
        ],
        "tips": [
            {"title": "Nutritious Diet", "text": "Prioritize whole, fresh foods and minimize processed snacks for a strong immune foundation."},
            {"title": "Adequate Sleep", "text": "Ensure children get the recommended hours of sleep for their age to support growth and behavior."},
            {"title": "Outdoor Play", "text": "Regular physical activity and sunshine are essential for Vitamin D and mental health."},
            {"title": "Consistent Routine", "text": "Children thrive on predictable schedules, which helps reduce stress and behavioral flare-ups."}
        ],
        "faqs": [
            {"q": "Are the remedies safe for newborn babies?", "a": "Yes, homeopathic remedies are extremely safe and non-invasive, making them ideal even for newborns."},
            {"q": "How do children take the medicine?", "a": "They are usually small, sweet pills that dissolve easily in the mouth or can be dissolved in a little water."},
            {"q": "Can it help with behavioral issues like ADHD?", "a": "Homeopathy addresses the child's constitutional makeup to help improve focus and emotional regulation naturally."}
        ]
    },
    {
        "id": "kidney",
        "filename": "treatment-kidney.html",
        "title": "Kidney & Urinary",
        "title_lower": "kidney and urinary",
        "image": "assets/images/hero-slide-1.png", # placeholder
        "subtitle": "Gentle support for urinary tract health, kidney function, and recurring infections by strengthening natural immunity.",
        "intro_html": "<p>The kidneys and urinary tract are responsible for vital blood filtration and waste elimination. Dr. Riddhi Mayani treats urological conditions holistically, understanding that recurrent infections or stones are signs of a systemic susceptibility.</p><p>By utilizing specific homeopathic treatments aimed at modifying the body's internal environment and supporting urinary tract health, we help the body manage functional challenges safely and effectively.</p>",
        "what_is_html": "<p>Kidney and Urinary conditions encompass functional and restorative disorders affecting the kidneys, bladder, and urinary passages.</p><p>They frequently manifest as recurrent infections, stones, or bladder sensitivity. These conditions can disrupt daily comfort and require a careful, systemic therapeutic approach.</p>",
        "symptoms": [
            "Frequent, urgent, or exceptionally painful urination",
            "Sharp, sudden pain in the lower back or side (flank pain)",
            "Presence of cloudiness or abnormal odor in the urine",
            "Inability to completely empty the bladder or weak urinary flow",
            "Noticeable swelling in the legs or feet due to fluid retention"
        ],
        "causes": [
            "Systemic susceptibilities leading to recurrent infections",
            "High concentration of specific minerals (calcium, oxalate) forming stones",
            "Hormonal fluctuations associated with aging",
            "Chronic dehydration and poor flushing of the renal system",
            "Underlying structural or metabolic factors"
        ],
        "tips": [
            {"title": "Hydrate Often", "text": "Drink at least 2-3 liters of water daily to help flush the kidneys and urinary tract."},
            {"title": "Reduce Salt", "text": "Limit sodium intake to minimize fluid retention and reduce the risk of stone formation."},
            {"title": "Maintain pH", "text": "A diet rich in citrus fruits and berries can help maintain a healthy urinary pH balance."},
            {"title": "Prompt Action", "text": "Do not ignore early signs of discomfort; early homeopathic support is key."}
        ],
        "faqs": [
            {"q": "Can homeopathy prevent recurring kidney stones?", "a": "Yes, homeopathy addresses the metabolic imbalance that leads to stone formation to prevent recurrence."},
            {"q": "Is it effective for chronic UTIs?", "a": "Homeopathy strengthens the local immunity of the urinary tract to break the cycle of infection naturally."},
            {"q": "Does it support kidney function?", "a": "By managing underlying stressors and inflammation, it helps preserve and support long-term renal health."}
        ]
    },
    {
        "id": "hair",
        "filename": "treatment-hair.html",
        "title": "Hair Health",
        "title_lower": "hair and scalp",
        "image": "assets/images/treat-hair-bg.png",
        "subtitle": "Address the internal causes of hair loss and scalp issues through constitutional treatment and nutritional support.",
        "intro_html": "<p>Hair health is uniquely sensitive to the overall vitality of the body. Homeopathic treatment recognizes that issues—like excessive hair fall or scalp conditions—are often symptoms of internal metabolic or emotional factors.</p><p>Homeopathic medicine stimulates the hair follicles naturally by addressing stress, supporting hormonal balance, and improving nutritional absorption, resulting in robust, healthy natural growth.</p>",
        "what_is_html": "<p>Hair and Scalp disorders represent conditions that disrupt the natural growth cycle or cause scalp irritation.</p><p>These conditions include Alopecia (patchy loss), pattern thinning, chronic dandruff, and scalp sensitivity. They often require a deep-rooted physiological balance to resolve effectively.</p>",
        "symptoms": [
            "Noticeable, excessive daily hair shedding or sudden bald patches",
            "Gradual thinning specifically on the crown or widening of the part",
            "Intensely itchy, flaky, red, or inflamed scalp skin",
            "Hair feeling abnormally brittle, dry, and breaking easily",
            "Lack of new hair growth replacing naturally shed hair"
        ],
        "causes": [
            "Severe physical or emotional stress triggering the shedding phase",
            "Hormonal shifts correlated with pregnancy or menopause",
            "Genetic predispositions contributing to pattern thinning",
            "Nutritional deficiencies (especially iron, Zinc, and B-vitamins)",
            "Systemic immune responses affecting the scalp"
        ],
        "tips": [
            {"title": "Scalp Massage", "text": "Gently massage your scalp with natural oils to improve blood circulation to the follicles."},
            {"title": "Avoid Excess Heat", "text": "Limit the use of blow dryers and flat irons which can cause mechanical damage and breakage."},
            {"title": "Iron-Rich Foods", "text": "Ensure your diet includes enough iron and biotin to provide the nutrients needed for growth."},
            {"title": "Hydration", "text": "Drink enough water to keep the hair shaft hydrated from within and prevent brittle hair."}
        ],
        "faqs": [
            {"q": "Can homeopathy stop rapid hair fall?", "a": "Yes, by identifying and treating the underlying emotional or hormonal trigger, hair fall often stabilizes within weeks."},
            {"q": "Is it safe for colored or chemically treated hair?", "a": "Homeopathy works internally, so it is perfectly safe regardless of your external hair treatments."},
            {"q": "Will it help with Alopecia patches?", "a": "Homeopathy addresses the immune system's role in Alopecia Areata to encourage natural regrowth."}
        ]
    }
]

def render_list(items):
    html = ""
    for item in items:
        html += f'''
            <li class="fade-in" style="display: flex; align-items: flex-start; gap: var(--space-3); padding: var(--space-4); background: var(--white); border-radius: var(--radius-lg); border: 1px solid var(--border); box-shadow: var(--shadow-sm);">
              <svg viewBox="0 0 24 24" fill="none" stroke="var(--primary)" stroke-width="2" stroke-linecap="round" style="width: 20px; height: 20px; flex-shrink: 0; margin-top: 2px;"><polyline points="20 6 9 17 4 12"/></svg>
              <span style="font-size: 1rem; line-height: 1.5; color: var(--text-color);">{item}</span>
            </li>'''
    return html

def render_tips(tips):
    html = ""
    for tip in tips:
        html += f'''
        <div class="tip-card fade-in">
          <h4>{tip["title"]}</h4>
          <p>{tip["text"]}</p>
        </div>'''
    return html

def render_faqs(faqs):
    html = ""
    for i, faq in enumerate(faqs):
        html += f'''
        <div class="faq-acc-item fade-in">
          <button class="faq-acc-trigger" id="faq-trigger-{i}">
            <span>{faq["q"]}</span>
            <svg class="faq-acc-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-acc-content">
            <p>{faq["a"]}</p>
          </div>
        </div>'''
    return html

# 1. Read the base template from we-treat.html
with open('we-treat.html', 'r', encoding='utf-8') as f:
    base_html = f.read()

# Separate head/nav and footer
try:
    head_nav, rest = base_html.split('<!-- Page Header -->', 1)
    _, footer = rest.split('<!-- Footer -->', 1)
    footer = '  <!-- Footer -->' + footer
except ValueError:
    print("Error splitting template.")
    exit(1)

# 2. Generate all 9 pages
for cat in categories:
    content = f'''  <!-- Page Header -->
  <section class="page-header" id="treatment-header">
    <div class="container">
      <nav class="breadcrumb" aria-label="Breadcrumb"><a href="index.html">Home</a><span class="breadcrumb__separator">›</span><a href="we-treat.html">We Treat</a><span class="breadcrumb__separator">›</span><span>{cat["title"]}</span></nav>
      <h1>{cat["title"]}</h1>
      <p class="subtitle subtitle--centered">{cat["subtitle"]}</p>
    </div>
  </section>

  <!-- Section 1: Intro -->
  <section class="section" id="intro">
    <div class="container">
      <div class="about-story" style="align-items: center; gap: var(--space-12);">
        <div class="about-story__content fade-in" style="flex: 1.2;">
          <div class="section-header" style="text-align: left; margin-bottom: var(--space-6);">
            <span class="label">Overview</span>
            <h2>Homeopathic Approach to {cat["title"]}</h2>
          </div>
          <div class="content" style="font-size: 1.1rem; line-height: 1.8; color: var(--text-color);">
            {cat["intro_html"]}
          </div>
        </div>
        <div class="about-story__image fade-in" style="flex: 0.8; max-width: 450px;">
          <img src="{cat["image"]}" alt="{cat["title"]} health" style="border-radius: var(--radius-2xl); box-shadow: var(--shadow-xl); width: 100%; height: auto; object-fit: cover;">
        </div>
      </div>
    </div>
  </section>

  <!-- Section 2: What Are They -->
  <section class="section section--sage" id="what-are-they">
    <div class="container">
      <div style="max-width: 800px; margin: 0 auto;">
         <h2 style="margin-bottom: var(--space-4);">What are {cat["title"]}?</h2>
         <div class="content fade-in" style="font-size: 1.1rem; line-height: 1.8; color: var(--text-color);">
           {cat["what_is_html"]}
         </div>
      </div>
    </div>
  </section>

  <!-- Section 3: Symptoms and Causes -->
  <section class="section" id="symptoms-causes">
    <div class="container">
      <div class="about-story fade-in" style="align-items: flex-start; margin-top: 0; gap: var(--space-12); flex-wrap: wrap;">
        <div class="about-story__content fade-in stagger-1" style="flex: 1; min-width: 280px;">
          <h2 style="margin-bottom: var(--space-6);">Common Symptoms</h2>
          <ul style="list-style-type: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: var(--space-4);">
            {render_list(cat["symptoms"])}
          </ul>
        </div>
        <div class="about-story__content fade-in stagger-2" style="flex: 1; min-width: 280px;">
          <h2 style="margin-bottom: var(--space-6);">Root Causes</h2>
          <ul style="list-style-type: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: var(--space-4);">
            {render_list(cat["causes"])}
          </ul>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 4: Expert Tips (Prevention) -->
  <section class="section tips-section" id="expert-tips">
    <div class="container">
      <div class="section-header fade-in">
        <span class="label">Living Better</span>
        <h2>Expert Tips for {cat["title"]} Prevention</h2>
        <p class="subtitle subtitle--centered">Incorporate these simple habits to support your recovery and maintain long-term wellness.</p>
      </div>
      <div class="tips-grid">
        {render_tips(cat["tips"])}
      </div>
    </div>
  </section>

  <!-- Section 5: FAQ -->
  <section class="section" id="faq">
    <div class="container">
      <div class="section-header fade-in">
        <span class="label">FAQ</span>
        <h2>Frequently Asked Questions</h2>
        <p class="subtitle subtitle--centered">Common questions patients ask about our homeopathic approach to {cat["title_lower"]}.</p>
      </div>
      <div class="faq-accordion">
        {render_faqs(cat["faqs"])}
      </div>
    </div>
  </section>

  <!-- Section 6: CTA -->
  <section class="section section--sage" id="cta-section">
    <div class="container">
      <div class="cta-banner fade-in">
        <h2>Ready to Find Natural Relief?</h2>
        <p>Book a consultation to receive a highly individualized homeopathic treatment plan targeting the root cause of your {cat["title_lower"]} conditions.</p>
        <div style="display: flex; gap: var(--space-4); justify-content: center; flex-wrap: wrap;">
          <a href="contact.html" class="btn btn--gold btn--lg">Book Consultation</a>
          <a href="about-homeopathy.html" class="btn btn--outline-light btn--lg">Learn About Homeopathy</a>
        </div>
      </div>
    </div>
  </section>

'''
    
    full_html = head_nav + content + footer
    with open(cat["filename"], 'w', encoding='utf-8') as f:
        f.write(full_html)
    print(f"Generated {cat['filename']}")

print("All treatment pages generated successfully with Images, Tips and FAQs!")
