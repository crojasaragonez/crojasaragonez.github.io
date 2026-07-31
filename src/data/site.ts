export const site = {
  name: 'Carlos Luis Rojas Aragonés',
  title: 'Technology Entrepreneur',
  tagline:
    'Co-Founder & Chief AI Officer at Subaxa. Building AI-native products and leading engineering organizations across the Americas.',
  description:
    'Technology entrepreneur and executive with 18+ years leading software organizations, AI initiatives, and nearshore delivery for clients across the United States and the Americas.',
  location: 'San Carlos, Costa Rica',
  socials: {
    linkedin: 'https://www.linkedin.com/in/crojasaragonez',
    github: 'https://github.com/crojasaragonez',
  },
  resumePath: '/resume.pdf',
  impact: [
    { value: '18+', label: 'Years in technology' },
    { value: '100+', label: 'Engineers scaled' },
    { value: '30%', label: 'Revenue from AI division' },
    { value: 'F500', label: 'Enterprise delivery' },
  ],
  about: {
    lead: 'I build technology organizations and AI-native products that ship.',
    paragraphs: [
      'I started as an engineer shipping product under tight timelines, then spent years owning delivery for distributed teams serving clients in the United States and across the Americas. As CTO, I scaled an engineering organization from zero to more than 100 engineers, built leadership layers that outlast any single hire, and stood up an AI division that grew to roughly 30% of company revenue.',
      'Today I am Co-Founder and Chief AI Officer at Subaxa, an AI-native proptech company transforming how people invest in judicial real estate auctions. We do not bolt AI onto an existing product — we design processes, decisions, and customer interactions around it from day one.',
      'I care about talent systems, clear technical strategy, and execution that founders and enterprise leaders can trust. I also teach, speak, and contribute to the open-source community when it sharpens the craft.',
    ],
  },
  expertise: [
    {
      title: 'AI product & strategy',
      description:
        'Designing AI-native products and organizations — from GenAI initiatives to revenue-bearing AI services — with clear business outcomes.',
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
    'Software Engineering Professor at Universidad Técnica Nacional (2014–2022), guiding student teams from idea validation to MVP.',
} as const;
