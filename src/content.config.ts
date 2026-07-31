import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

const blog = defineCollection({
  loader: glob({ base: './src/content/blog', pattern: '**/*.{md,mdx}' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.coerce.date(),
    updatedDate: z.coerce.date().optional(),
    draft: z.boolean().optional().default(false),
  }),
});

const talks = defineCollection({
  loader: glob({ base: './src/content/talks', pattern: '**/*.{md,mdx}' }),
  schema: z.object({
    title: z.string(),
    event: z.string(),
    topic: z.string(),
    description: z.string().optional(),
    date: z.coerce.date().optional(),
    location: z.string().optional(),
    url: z.string().url().optional(),
    featured: z.boolean().optional().default(false),
    order: z.number().optional().default(0),
  }),
});

const testimonials = defineCollection({
  loader: glob({ base: './src/content/testimonials', pattern: '**/*.{md,mdx}' }),
  schema: z.object({
    quote: z.string(),
    name: z.string(),
    role: z.string(),
    company: z.string().optional(),
    order: z.number().optional().default(0),
  }),
});

export const collections = { blog, talks, testimonials };
