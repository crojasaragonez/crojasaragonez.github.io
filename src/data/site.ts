import golabsOffice from '../assets/golabs_office.avif';
import subaxaTeam from '../assets/subaxa_team.jpg';

export const site = {
  name: 'Carlos Luis Rojas Aragonés',
  title: 'Technology Entrepreneur',
  tagline:
    'Co-Founder & Chief AI Officer at Subaxa. Co-founder and board member at Golabs. Building AI-native products across the Americas.',
  description:
    'Technology entrepreneur and executive with 16+ years leading software organizations, AI initiatives, and nearshore delivery. Co-founder of Golabs and Subaxa.',
  location: 'San Carlos, Costa Rica',
  socials: {
    linkedin: 'https://www.linkedin.com/in/crojasaragonez',
    github: 'https://github.com/crojasaragonez',
  },
  resumePath: '/resume.pdf',
  impact: [
    { value: '16+', label: 'Years in technology' },
    { value: '100+', label: 'Engineers scaled' },
    { value: '30%', label: 'Revenue from AI division' },
    { value: 'F500', label: 'Enterprise delivery' },
  ],
  about: {
    lead: 'I build technology organizations and AI-native products that ship.',
    summary:
      'From shipping product as an engineer to co-founding Golabs, scaling it past 100 engineers, and founding Subaxa: a trajectory across delivery, leadership, and AI-native entrepreneurship.',
    paragraphs: [
      'I started as an engineer shipping product under tight timelines, then co-founded Golabs in 2014. Over roughly twelve years as Delivery Manager and CTO, I helped grow a nearshore engineering company from a small founding team in San Carlos to 100+ engineers across Latin America, including an AI division that reached about 30% of company revenue. In 2023 I sold a majority stake and stayed on as CTO until 2026; today I serve on the Board of Directors.',
      'Today I am Co-Founder and Chief AI Officer at Subaxa, an AI-native proptech company transforming how people invest in judicial real estate auctions in Costa Rica. It is the shift from delivering AI services for others to building an AI-native product company with my founding partners, with processes, decisions, and customer interactions designed around intelligence from day one.',
      'I care about talent systems, clear technical strategy, and execution that founders and enterprise leaders can trust. I also teach, speak, and contribute to the open-source community when it sharpens the craft.',
    ],
  },
  ventures: [
    {
      slug: 'golabs',
      name: 'Golabs',
      role: 'Co-Founder · Board of Directors',
      period: '2014 - Present',
      location: 'San Carlos & San José, Costa Rica · LATAM',
      website: 'https://golabstech.com',
      websiteLabel: 'golabstech.com',
      tagline: 'Nearshore AI and engineering talent from Latin America.',
      summary:
        'The company I co-founded in 2014, grew for twelve years as Delivery Manager and CTO, and continue to serve as a board member after selling a majority stake in 2023.',
      story: [
        'Golabs started in San Carlos, Costa Rica, with a small founding team and a clear bet: build durable nearshore engineering capacity in LATAM for companies that need more than extra hands. They need accountable teams.',
        'I spent the early years as Delivery Manager, establishing how we estimated, staffed, and shipped for clients. As CTO I scaled the technical organization from essentially zero to more than 100 engineers across Costa Rica, Mexico, Nicaragua, Colombia, Guatemala, Argentina, the United States, and other markets, with leadership layers designed to outlast any single hire.',
        'We stood up an AI division that grew to roughly 30% of company revenue, pairing custom AI systems and nearshore delivery for enterprise and growth-stage clients. In 2023 I sold a majority of my shares and continued as CTO until 2026. Today I serve on the Board of Directors, staying connected to the company I helped build.',
      ],
      focus: [
        {
          title: 'Nearshore AI & engineering',
          description:
            'Dedicated LATAM teams embedded with clients: AI engineers, data scientists, and full-stack talent in overlapping U.S. time zones.',
        },
        {
          title: 'Custom AI systems',
          description:
            'From strategy to production: agents, ML models, orchestration, and the operating habits that keep initiatives from stalling as demos.',
        },
        {
          title: 'AI fluency',
          description:
            'Organization-wide enablement so teams can work alongside AI with shared language, judgment, and delivery discipline.',
        },
      ],
      milestones: [
        { label: 'Founded', detail: '2014 · San Carlos, Costa Rica' },
        { label: 'My roles', detail: 'Delivery Manager → CTO (~12 years)' },
        { label: 'Scale', detail: '0 → 100+ engineers across LATAM' },
        { label: 'AI division', detail: '~30% of company revenue' },
        { label: 'Majority sale', detail: '2023' },
        { label: 'Today', detail: 'Board of Directors' },
      ],
      image: {
        src: golabsOffice,
        alt: 'Golabs office in Ciudad Quesada, San Carlos',
        caption: 'Golabs office in Ciudad Quesada, San Carlos, Costa Rica.',
        label: 'Office',
        heading: 'Home base in Ciudad Quesada',
      },
      press: [
        {
          outlet: 'El Financiero',
          title:
            'Go-Labs, la startup de San Carlos que un estudio ubica como la segunda mejor firma para jóvenes en Costa Rica',
          url: 'https://www.elfinancierocr.com/pymes/historias/go-labs-la-startup-de-san-carlos-que-un-estudio/6QLEWQXF3FBMTDTT7Q7ZU4AZ7Y/story/',
          date: 'October 2021',
        },
      ],
    },
    {
      slug: 'subaxa',
      name: 'Subaxa',
      role: 'Co-Founder & Chief AI Officer',
      period: 'Present',
      location: 'San Carlos, Costa Rica',
      website: 'https://subaxa.com',
      websiteLabel: 'subaxa.com',
      tagline: 'AI-native proptech for judicial real estate auctions.',
      summary:
        'Where I moved from providing AI services to other companies to building an AI-native product company with my founding partners.',
      story: [
        'Subaxa is the company where the thesis became personal: stop only delivering AI capabilities for others, and build a product that cannot work without intelligence in the core loop.',
        'We focus on judicial real estate auctions (remates) in Costa Rica, a market where opportunity is real and information is fragmented. Investors need a national map of auctions, legal risk signal they can trust, and human experts who stay with them through the remate.',
        'As Co-Founder and Chief AI Officer, I lead how AI shapes product, process, and organization. Models help source, structure, score, and explain, alongside legal and investment specialists. The goal is not a chatbot bolted onto a listing site; it is an operating system for investing in remates with evidence instead of intuition.',
      ],
      focus: [
        {
          title: 'Opportunity map',
          description:
            'Nationwide visibility into remates. Explore the market in one place instead of chasing scattered edictos.',
        },
        {
          title: 'AI risk & value signal',
          description:
            'Models trained on the Costa Rican market to surface legal risk, estimated margins, and alerts before opportunities go wide.',
        },
        {
          title: 'Human + AI accompaniment',
          description:
            'Legal and investment specialists paired with the platform so investors arrive at the remate with a plan, not a guess.',
        },
      ],
      milestones: [
        { label: 'Model', detail: 'AI-native product company' },
        { label: 'Market', detail: 'Judicial remates · Costa Rica' },
        { label: 'My role', detail: 'Co-Founder & Chief AI Officer' },
        { label: 'Thesis', detail: 'Intelligence in the core loop, not a bolt-on' },
        { label: 'Team', detail: 'Legal · investment · product · AI' },
        { label: 'Base', detail: 'San Carlos, Alajuela' },
      ],
      image: {
        src: subaxaTeam,
        alt: 'Founding team of Subaxa',
        caption:
          'Founders of Subaxa. Standing, left to right: Dennis Valverde and Christopher Aguilar. Seated, left to right: José Mora, Cindy Herrera, Carlos Rojas and Nelson Ugalde.',
        label: 'Team',
        heading: 'The founding team',
      },
      press: [
        {
          outlet: 'El Financiero',
          title:
            '¿Le interesa comprar propiedades en remate en Costa Rica? Esta herramienta las identifica y permite determinar cuáles le convienen',
          url: 'https://www.elfinancierocr.com/tecnologia/le-interesa-comprar-propiedades-en-remate-en-costa/JMBYACBI5FGFVDMBEBAPDKIJUM/story/',
          date: 'July 2026',
        },
      ],
    },
  ],
  experience: [
    {
      company: 'Subaxa',
      role: 'Co-Founder & Chief AI Officer',
      location: 'Costa Rica',
      period: 'Present',
      highlights: [
        'Lead product and AI strategy for an AI-native proptech company focused on judicial real estate auctions in Costa Rica.',
        'Design processes, decisions, and customer interactions around artificial intelligence from day one, not as a bolt-on feature.',
        'Build the technical and organizational foundations for an AI-first operating model with founding partners.',
      ],
    },
    {
      company: 'Golabs',
      role: 'Board of Directors',
      location: 'LATAM',
      period: '2023 - Present',
      highlights: [
        'Joined the board after selling a majority stake in 2023, serving alongside the CTO role until stepping out of it in 2026.',
        'Support strategic direction for a nearshore AI and engineering organization serving clients across the Americas.',
      ],
    },
    {
      company: 'Golabs',
      role: 'Co-Founder & Chief Technology Officer',
      location: 'LATAM',
      period: '2019 - July 2026',
      highlights: [
        'Created and led the AI division, achieving roughly 30% of total company revenue through AI services and solutions.',
        'Stayed on as CTO for three years after the 2023 majority sale, leading technology through the ownership transition.',
        'Scaled the company from 0 to 100+ engineers across Latin America, supporting complex, high-impact projects for Fortune 500 clients.',
        'Acted as a strategic partner to executive leadership and clients, translating business objectives into technical roadmaps and execution plans.',
        'Built leadership layers (tech leads, managers, directors) to sustain growth beyond 100+ engineers.',
        'Designed and implemented distributed team structures across Costa Rica, Mexico, Nicaragua, Colombia, Guatemala, Argentina, the United States, and other LATAM countries.',
        'Led hiring, organizational design, and leadership development for high-performance, multicultural engineering teams.',
      ],
    },
    {
      company: 'Golabs',
      role: 'Co-Founder & Delivery Manager',
      location: 'Costa Rica',
      period: '2014 - 2019',
      highlights: [
        'Co-founded Golabs and led end-to-end delivery for multiple client engagements, establishing repeatable processes across distributed teams.',
        'Standardized delivery processes across projects, increasing consistency and reducing onboarding time for new team members.',
        'Partnered with sales and pre-sales teams to estimate effort, define delivery approaches, and support successful deal closures.',
        'Mentored technical leads and senior engineers, strengthening delivery ownership and decision-making at the team level.',
      ],
    },
    {
      company: 'Universidad Técnica Nacional',
      role: 'Software Engineering Professor',
      location: 'Costa Rica',
      period: '2014 - 2022',
      highlights: [
        'Guided student teams in launching startup projects from idea validation to MVP development and demo presentations.',
        'Fostered a hands-on learning environment through project-based coursework, hackathons, and real client simulations.',
        'Created and shared open educational resources, code samples, and technical workshops beyond the classroom.',
        'Integrated entrepreneurship and real-world product development into software engineering curricula.',
      ],
    },
    {
      company: 'Avantica',
      role: 'Software Engineer',
      location: 'Costa Rica',
      period: '2011 - 2014',
      highlights: [
        'Owned end-to-end feature development from design through deployment, consistently meeting or exceeding client expectations.',
        'Supported multiple client engagements while maintaining high productivity and delivery standards.',
        'Embedded quickly into client engineering teams, delivering production-quality features across diverse tech stacks and processes.',
      ],
    },
    {
      company: 'NCQ Solution',
      role: 'Software Developer',
      location: 'Costa Rica',
      period: '2010 - 2011',
      highlights: [
        'Joined at an early stage and helped build the initial product from concept to first paying customers.',
        'Designed and implemented core system architecture that scaled as the company grew.',
        'Delivered early MVP features under tight timelines, enabling rapid market validation.',
        'Took ownership of critical components that became foundational to long-term success.',
      ],
    },
  ],
  highlights: [
    {
      title: 'Strategy & execution',
      description:
        'Defined technical strategy aligned with business growth and enterprise client needs across the United States and the Americas.',
    },
    {
      title: 'Engineering leadership',
      description:
        'Built and led large-scale, distributed engineering organizations across LATAM with durable leadership layers.',
    },
    {
      title: 'Global delivery',
      description:
        'Delivered software solutions for Fortune 500 companies using nearshore and distributed models.',
    },
    {
      title: 'Talent development',
      description:
        'Established hiring pipelines, career paths, and leadership structures for senior and junior engineers alike.',
    },
    {
      title: 'Technical speaking',
      description:
        'Delivered technology talks and presentations on AI, cloud delivery, and engineering leadership.',
    },
    {
      title: 'Open source',
      description:
        'Contributor to the Ruby ecosystem and other community-driven projects.',
    },
  ],
  expertise: [
    {
      title: 'AI product & strategy',
      description:
        'Designing AI-native products and organizations, from GenAI initiatives to revenue-bearing AI services, with clear business outcomes.',
    },
    {
      title: 'Cloud-native platforms',
      description:
        'Architecting and scaling systems on AWS: resilient web platforms, data pipelines, and production-ready cloud foundations.',
    },
    {
      title: 'Org design & talent',
      description:
        'Hiring pipelines, career paths, and leadership layers that let engineering organizations grow past 100 people without collapsing.',
    },
    {
      title: 'Nearshore delivery',
      description:
        'Distributed teams across LATAM and the US delivering mission-critical software for Fortune 500 and growth-stage companies.',
    },
  ],
  // Concrete technologies, grouped for scanning. Every entry should be something
  // I have shipped or taught: most map to a talk in src/content/talks.
  stack: [
    {
      group: 'AI & agents',
      items: [
        'LLM agents',
        'Multi-agent systems',
        'RAG pipelines',
        'Vector databases',
        'Prompt & context engineering',
      ],
    },
    {
      group: 'Cloud & infrastructure',
      items: ['AWS', 'Serverless & FaaS', 'Docker & Compose', 'Terraform / IaC', 'Linux & systemd'],
    },
    {
      group: 'APIs & distributed systems',
      items: [
        'REST API design',
        'GraphQL & Apollo',
        'Message queues',
        'Event-driven architecture',
        'SSR / SSG / CSR',
      ],
    },
    {
      group: 'Languages & runtimes',
      items: ['Python', 'JavaScript & TypeScript', 'Node.js', 'Ruby', 'PHP / Laravel'],
    },
  ],
  education: [
    {
      school: 'Massachusetts Institute of Technology',
      program: 'Executive Program: Chief Technology Officer',
      year: '2026',
    },
    {
      school: 'Texas Tech University',
      program: 'Machine Learning & Data Science Program',
      year: '2025',
    },
    {
      school: 'Universidad Técnica Nacional',
      program: 'Bachelor’s Degree in Software Engineering',
      year: '2013',
    },
  ],
  teaching:
    'Software Engineering Professor at Universidad Técnica Nacional (2014-2022), guiding student teams from idea validation to MVP.',
  skills: {
    technical: [
      'Cloud-native architectures (AWS)',
      'Scalable systems',
      'Data & AI platforms',
      'Organizational design',
      'Nearshore delivery',
    ],
    languages: [
      { name: 'English', level: 'C1' },
      { name: 'Spanish', level: 'Native' },
    ],
    interests: ['Open Source', 'Artificial Intelligence', 'Entrepreneurship'],
  },
} as const;
