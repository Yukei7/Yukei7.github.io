import heroAvatar from '../assets/images/avatar.jpg';
import type { SiteConfig } from '../types';

const siteConfig: SiteConfig = {
    title: 'Yuqi Yan',
    description: 'Technical notes on distributed systems, programming language, statistics and machine learning.',
    primaryNavLinks: [
        {
            text: 'Home',
            href: '/'
        },
        {
            text: 'Blog',
            href: '/blog'
        },
        {
            text: 'Tags',
            href: '/tags'
        },
        {
            text: 'About',
            href: '/about'
        },
        {
            text: 'Resume',
            href: '/resume'
        }
    ],
    secondaryNavLinks: [
        {
            text: 'Blog',
            href: '/blog'
        },
        {
            text: 'Tags',
            href: '/tags'
        },
        {
            text: 'About',
            href: '/about'
        },
        {
            text: 'Resume',
            href: '/resume'
        }
    ],
    socialLinks: [
        {
            text: 'GitHub',
            href: 'https://github.com/Yukei7',
            icon: 'github'
        },
        {
            text: 'LinkedIn',
            href: 'https://www.linkedin.com/in/yukei7/',
            icon: 'linkedin'
        },
        {
            text: 'Instagram',
            href: 'https://www.instagram.com/yukeiyim',
            icon: 'instagram'
        }
    ],
    hero: {
        title: 'Hi there!',
        text: "I'm Yuqi Yan, a software engineer focusing on distributed storage systems at Uber. This site is primarily a personal technical blog covering distributed systems, programming language, statistics and machine learning topics worth revisiting.",
        avatar: {
            src: heroAvatar,
            alt: 'Yuqi Yan'
        }
    },
    subscribe: {
        enabled: false
    },
    postsPerPage: 5
};

export default siteConfig;
