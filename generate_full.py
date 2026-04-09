import os
import re

# Data structure for all 9 treatment categories
categories = [
    {
        "id": "skin",
        "filename": "treatment-skin.html",
        "title": "Skin Diseases",
        "title_lower": "skin",
        "subtitle": "Clear, radiantly healthy skin achieved by treating constitutional imbalances rather than suppressing topical symptoms.",
        "intro_html": "<p>Dr. Riddhi Mayani treats skin conditions through a holistic approach. Homeopathy believes in treating skin issues from within to achieve a lasting internal balance rather than temporary external relief.. Homeopathy believes that the skin is a mirror of internal health.</p><p>By understanding your entire medical history, stress levels, immunity, and genetics, we prescribe gentle, individualized remedies that aim to resolve the root disturbance. This approach offers safe, long-lasting relief from persistent skin disorders with gentle, root-cause focused care.</p>",
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
        ]
    },
    {
        "id": "respiratory",
        "filename": "treatment-respiratory.html",
        "title": "Respiratory Conditions",
        "title_lower": "respiratory",
        "subtitle": "Breathe easier with natural, non-habit-forming homeopathic care that strengthens your respiratory system's immunity.",
        "intro_html": "<p>Respiratory issues, whether acute like the seasonal flu or chronic like asthma, can severely impact your quality of life. Dr. Riddhi Mayani utilizes highly customized homeopathic formulations to naturally reduce hypersensitivity in the respiratory tract.</p><p>Unlike inhalers or antihistamines that only offer temporary suppression, our treatments focus on building respiratory resilience and boosting your immune system’s natural defenses against allergens, pollutants, and weather changes.</p>",
        "what_is_html": "<p>Respiratory conditions encompass disorders affecting the lungs, airways, sinuses, and nasal passages. They involve the inflammation or obstruction of the respiratory tract, making breathing difficult, painful, or uncomfortable.</p><p>These conditions range from allergic rhinitis (hay fever) and chronic sinusitis to deeper issues like bronchitis and asthma. They are predominantly triggered by hyper-reactive immune responses or recurrent chronic infections.</p>",
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
        ]
    },
    {
        "id": "digestive",
        "filename": "treatment-digestive.html",
        "title": "Digestive Disorders",
        "title_lower": "digestive",
        "subtitle": "Restore gut health and digestive harmony with individualized remedies that address underlying gastrointestinal dysfunction.",
        "intro_html": "<p>The digestive system is the core of our overall health. The homeopathic approach to digestive disorders focuses heavily on the gut-brain axis and your constitutional makeup. Dr. Riddhi Mayani thoroughly investigates not just what you eat, but how your body processes stress and emotions.</p><p>By treating the individual rather than just the localized inflammation, our homeopathic remedies soothe gut linings, improve enzymatic function, and promote lasting rhythmic bowel harmony without the need for lifetime systemic dependence.</p>",
        "what_is_html": "<p>Digestive disorders refer to a wide spectrum of health issues occurring anywhere in the gastrointestinal (GI) tract, from the esophagus and stomach to the intestines and liver.</p><p>Conditions such as Irritable Bowel Syndrome (IBS), Acid Reflux (GERD), and Ulcerative Colitis are increasingly common. They disrupt the body’s ability to digest food, absorb vital nutrients, and successfully eliminate waste, drastically impacting energy levels and comfort.</p>",
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
            "Disruption of the gut microbiome (dysbiosis)",
            "Sedentary lifestyle and lack of adequate hydration",
            "Underlying autoimmune or inflammatory disease markers"
        ]
    },
    {
        "id": "mental",
        "filename": "treatment-mental.html",
        "title": "Mental & Emotional Health",
        "title_lower": "mental and emotional",
        "subtitle": "Gentle, comprehensive care for psychological well-being that tackles root emotional traumas without internal reliance.",
        "intro_html": "<p>Mental health is a vital constituent of an individual's general well-being. Dr. Riddhi Mayani takes a deeply holistic approach to mental and emotional disorders. Recognizing the deep link between mind and body, homeopathy aims at healing the mind-body connection from its root.</p><p>Homeopathy works by evaluating your state of health, emotions, specific fears, and precise mind-frame. By utilizing natural micro-doses, it gently activates the body's intrinsic ability to balance neurotransmitters and process unresolved mental blockages.</p>",
        "what_is_html": "<p>Mental diseases are conditions of the mind that fundamentally alter a person’s mood, emotional processing, cognitive thoughts, and behavior. These states can severely reduce an individual’s ability to handle everyday tasks, maintain relationships, and sustain stability.</p><p>Common conditions targeted by homeopathy include Generalized Anxiety, Clinical Depression, OCD, Panic Attacks, PTSD, and severe Insomnia. Homeopathic medicine has historically shown profound efficacy in treating these states gently and without dependency concerns or harsh systemic effects.</p>",
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
        ]
    },
    {
        "id": "joint",
        "filename": "treatment-joint.html",
        "title": "Joint & Musculoskeletal",
        "title_lower": "joint and bone",
        "subtitle": "Manage chronic pain, stiffness, and degenerative conditions naturally by supporting the body's intrinsic restorative power.",
        "intro_html": "<p>Joint and musculoskeletal pain can strip away your mobility and joy. Homeopathy offers a gentle, non-invasive approach that focuses on long-term relief and metabolic recovery. At GeneticHomeopathy, Dr. Riddhi Mayani provides a profoundly safer alternative.</p><p>Homeopathic therapies focus on reducing systemic inflammation, slowing down joint degeneration, and improving the absolute mobility of the patient. The individualized remedies uniquely target precise types of pain—whether it is tearing, aching, burning, or stiffness worst in the morning.</p>",
        "what_is_html": "<p>Joint and musculoskeletal disorders affect the bones, muscles, ligaments, tendons, and joints of the human body. These conditions inherently impair movement, drastically reduce flexibility, and guarantee a persistent spectrum of pain.</p><p>Ranging from wear-and-tear conditions like Osteoarthritis and Cervical Spondylosis to autoimmune inflammatory responses like Rheumatoid Arthritis or Gout, musculoskeletal diseases require comprehensive structural and metabolic management.</p>",
        "symptoms": [
            "Deep, aching, or sharp pain in major joints (knees, hips, shoulders)",
            "Pronounced morning stiffness that restricts immediate mobility",
            "Visible swelling, redness, or heat emanating from the joint",
            "Restricted range of motion or an absolute inability to bend",
            "Numbness, tingling, or radiating nerve pain (like Sciatica)"
        ],
        "causes": [
            "Progressive wear and tear of cartilage due to age or overuse",
            "Autoimmune conditions where the body aggressively attacks joint tissue",
            "Metabolic disorders leading to uric acid crystal deposition (Gout)",
            "Historical physical injuries, strains, fractures, or blunt trauma",
            "Poor posture, sedentary habits, and nutritional calcium/vitamin D deficiency"
        ]
    },
    {
        "id": "women",
        "filename": "treatment-women.html",
        "title": "Women's Health",
        "title_lower": "women's health",
        "subtitle": "Safe, hormone-free treatment designed specifically for female reproductive and hormonal health across every life stage.",
        "intro_html": "<p>A woman's body undergoes extraordinary, complex hormonal shifts throughout her life. Dr. Riddhi Mayani provides deeply empathetic and specialized care utilizing purely natural homeopathic medicines that gently regulate the endocrine system.</p><p>Our holistic treatments work in harmony with the female body to balance hormones naturally, our holistic methodology balances the hormones naturally, respecting the intricate rhythm of the female body to restore true well-being.</p>",
        "what_is_html": "<p>Women's health conditions refer broadly to gynecological, reproductive, and hormonal disorders specifically affecting female anatomy and the endocrine cycle.</p><p>These cover a wide spectrum of deeply impactful conditions including PCOS (Polycystic Ovary Syndrome), severe Dysmenorrhea (Painful Periods), Endometriosis, Uterine Fibroids, debilitating Menopause symptoms, and underlying complications related to infertility or thyroid dysfunction.</p>",
        "symptoms": [
            "Extremely painful, irregular, exceptionally heavy, or absent menstrual cycles",
            "Severe pelvic pain, cramping, or generalized lower abdominal heaviness",
            "Intense hot flashes, night sweats, and aggressive mood fluctuations",
            "Unexplained weight gain, persistent acne, or disruptive facial hair growth",
            "Challenges related to natural conception and maintaining pregnancy"
        ],
        "causes": [
            "Systemic hormonal imbalances (estrogen dominance, progesterone deficiency)",
            "Thyroid gland dysfunction significantly impacting the metabolic rate",
            "High levels of physiological stress severely disrupting the menstrual cycle",
            "Genetic predispositions toward fibroids, cysts, or endometriosis",
            "Underlying nutritional deficiencies and autoimmune markers"
        ]
    },
    {
        "id": "children",
        "filename": "treatment-pediatric.html",
        "title": "Pediatric Care",
        "title_lower": "pediatric",
        "subtitle": "Non-toxic, exceptionally gentle remedies perfectly safe for infants and children to build a foundation of lifelong immunity.",
        "intro_html": "<p>Children require exceptionally mild yet deeply effective medical care. Dr. Riddhi Mayani specializes in homeopathic pediatric treatments because they are exceptionally gentle, safe for all ages, and designed to support the body's natural healing processes effectively.</p><p>Because homeopathic pills are sweet and easily dissolved, they are simple to administer even to infants. Our treatments aim not only to resolve the immediate acute infection or behavioral issue but to fundamentally strengthen the child's developing immune and nervous systems.</p>",
        "what_is_html": "<p>Pediatric conditions involve the broad spectrum of physical, behavioral, and developmental ailments that affect infants, toddlers, and adolescents as they rapidly grow.</p><p>These range significantly from acute physical ailments like recurrent ear infections, teething pain, colic, and bedwetting, to complex developmental and behavioral challenges including ADHD, intense temper tantrums, autism spectrum support, and delayed milestones.</p>",
        "symptoms": [
            "Recurrent acute fevers, constant earaches, or repetitive sore throats",
            "Severe colic, infant acid reflux, or unexplained digestive upset",
            "Noticeable hyperactivity, complete inability to focus, or extreme impulsivity",
            "Frequent bedwetting (enuresis) in older children",
            "Delayed speech, delayed walking, or disrupted physical growth"
        ],
        "causes": [
            "An immature, actively developing, or hypersensitive immune system",
            "Genetic predispositions or strong familial history of allergies/atopies",
            "Nutritional malabsorption interfering with rapid physical development",
            "Environmental triggers, food intolerances, and heavy metal exposure",
            "Emotional sensitivities, anxiety, or disruptions in standard routines"
        ]
    },
    {
        "id": "kidney",
        "filename": "treatment-kidney.html",
        "title": "Kidney & Urinary",
        "title_lower": "kidney and urinary",
        "subtitle": "Gentle support for urinary tract health, kidney function, and recurring infections by strengthening natural immunity.",
        "intro_html": "<p>The kidneys and urinary tract are responsible for vital blood filtration and waste elimination. Dr. Riddhi Mayani treats urological conditions holistically, understanding that recurrent infections or kidney stones are signs of a systemic susceptibility rather than isolated events.</p><p>By utilizing specific homeopathic treatments aimed at modifying the body's internal environment and reducing urinary tract hypersensitivity, we can successfully break the cycle of recurrent UTIs and assist the body in naturally managing blockages or kidney function decline safely.</p>",
        "what_is_html": "<p>Kidney and Urinary conditions encompass a range of functional and infectious disorders affecting the kidneys, ureters, bladder, and urethra.</p><p>They manifest frequently as recurrent Urinary Tract Infections (UTIs), painful Kidney Stones, Interstitial Cystitis (painful bladder syndrome), or prostate enlargement (BPH) in older adults. These conditions severely disrupt daily comfort and require careful, restorative therapeutic management.</p>",
        "symptoms": [
            "Frequent, urgent, or exceptionally painful urination (burning sensation)",
            "Sharp, sudden, excruciating pain in the lower back or side (flank pain)",
            "Presence of blood, cloudiness, or a strong abnormal odor in the urine",
            "Inability to completely empty the bladder or weak urinary flow",
            "Noticeable swelling in the legs, ankles, or feet due to fluid retention"
        ],
        "causes": [
            "Recurrent bacterial invasions compounded by localized immune weakness",
            "High concentration of specific minerals (calcium, oxalate) forming stones",
            "Hormonal fluctuations naturally associated with aging (e.g., prostate enlargement)",
            "Chronic dehydration coupled with poor dietary choices and high sodium",
            "Underlying structural abnormalities in the urinary system"
        ]
    },
    {
        "id": "hair",
        "filename": "treatment-hair.html",
        "title": "Hair Health",
        "title_lower": "hair and scalp",
        "subtitle": "Address the internal causes of hair loss and scalp issues through constitutional treatment and nutritional support.",
        "intro_html": "<p>Hair health is uniquely sensitive to the overall vitality of the body. Homeopathic treatment for hair conditions recognizes that external issues—like excessive hair fall or scalp disease—are symptoms of deeper internal metabolic or emotional stress. Dr. Riddhi Mayani treats the whole person, not just the scalp.</p><p>Instead of relying on harsh chemical serums, homeopathic medicine stimulates the hair follicles naturally by addressing chronic stress, correcting hormonal imbalances, and repairing nutritional absorption, resulting in robust, healthy natural hair growth.</p>",
        "what_is_html": "<p>Hair and Scalp disorders represent conditions that disrupt the natural growth cycle of hair follicles or cause inflammation, flaking, and irritation on the skin of the scalp.</p><p>These conditions include widespread issues such as Alopecia Areata (patchy hair loss), Male/Female Pattern Baldness, severe chronic Dandruff, Scalp Psoriasis, and generalized diffuse hair thinning. They are often profoundly distressing and require a deep-rooted physiological fix.</p>",
        "symptoms": [
            "Noticeable, excessive daily hair shedding or sudden bald patches",
            "Gradual thinning of hair specifically on the crown or widening of the part",
            "Intensely itchy, flaky, red, or inflamed scalp skin",
            "Hair feeling abnormally brittle, dry, and breaking easily",
            "Lack of new hair growth replacing naturally shed hair"
        ],
        "causes": [
            "Severe physical or emotional stress triggering the shedding phase",
            "Hormonal shifts perfectly correlated with pregnancy, menopause, or thyroid disorders",
            "Genetic predispositions contributing to pattern baldness",
            "Nutritional deficiencies (especially iron, vitamin D, and B-vitamins)",
            "Autoimmune reactions where the body mistakenly attacks its own hair follicles"
        ]
    }
]

def render_list(items):
    html = ""
    for item in items:
        html += f'''
            <li class="fade-in" style="display: flex; align-items: flex-start; gap: var(--space-3); padding: var(--space-4); background: var(--white); border-radius: var(--radius-lg); border: 1px solid var(--border); box-shadow: var(--shadow-sm);">
              <svg viewBox="0 0 24 24" fill="none" stroke="var(--primary)" stroke-width="2" stroke-linecap="round" style="width: 24px; height: 24px; flex-shrink: 0; margin-top: 2px;"><polyline points="20 6 9 17 4 12"/></svg>
              <span style="font-size: 1.05rem; line-height: 1.5; color: var(--text-color);">{item}</span>
            </li>'''
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

# 2. Generate all 9 pages with the fixed CTA banner without inline styling!
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
      <div class="section-header fade-in">
        <span class="label">Overview</span>
        <h2>Homeopathic Approach to {cat["title"]}</h2>
      </div>
      <div class="content fade-in" style="max-width: 800px; margin: 0 auto; font-size: 1.1rem; line-height: 1.8; color: var(--text-color);">
        {cat["intro_html"]}
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
      <div class="about-story fade-in" style="align-items: flex-start; margin-top: 0; gap: var(--space-12);">
        <div class="about-story__content fade-in stagger-1" style="flex: 1; min-width: 300px;">
          <h2 style="margin-bottom: var(--space-6);">Common Symptoms</h2>
          <ul style="list-style-type: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: var(--space-4);">
            {render_list(cat["symptoms"])}
          </ul>
        </div>
        <div class="about-story__content fade-in stagger-2" style="flex: 1; min-width: 300px;">
          <h2 style="margin-bottom: var(--space-6);">Root Causes</h2>
          <ul style="list-style-type: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: var(--space-4);">
            {render_list(cat["causes"])}
          </ul>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 4: CTA -->
  <section class="section" id="cta-section">
    <div class="container">
      <div class="cta-banner fade-in">
        <h2>Ready to Find Natural Relief?</h2>
        <p>Book a consultation to receive a highly individualized homeopathic treatment plan targeting the root cause of your {cat["title_lower"]} conditions.</p>
        <div style="display: flex; gap: var(--space-4); justify-content: center; flex-wrap: wrap;">
          <a href="contact.html" class="btn btn--gold btn--lg">Book Free Consultation</a>
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

# 3. Update we-treat.html for Kidney and Hair specifically
print("Updating we-treat.html with Learn More buttons for Kidney and Hair...")
for cat in [c for c in categories if c["id"] in ["kidney", "hair"]]:
    pattern = r'(<div class="treat-category-section[^>]*data-category="' + cat["id"] + r'".*?<div class="treat-expand__list">.*?</div>)\s*</div>'
    match = re.search(pattern, base_html, flags=re.DOTALL)
    if match:
        original_inner = match.group(1)
        button_html = f'''
        <div style="margin-top: var(--space-8); display: flex; justify-content: center;">
          <a href="{cat["filename"]}" class="btn btn--primary" style="display: inline-flex; align-items: center; gap: var(--space-2);">
            Learn More About {cat["title"]} Care 
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" style="width: 16px; height: 16px;"><path d="M5 12h14"/><path d="M12 5l7 7-7 7"/></svg>
          </a>
        </div>'''
        new_block = original_inner + button_html + '\n      </div>'
        base_html = base_html.replace(match.group(0), new_block)
    else:
        print(f"Failed to find match for {cat['id']}")

with open('we-treat.html', 'w', encoding='utf-8') as f:
    f.write(base_html)
print("we-treat.html updated successfully!")
