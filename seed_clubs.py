from models import OrgType

CAMPUS_CLUBS = [
    {
        #1
        "club_name": "Accounting Society",
        "org_type": OrgType.ACADEMIC_PROFESSIONAL_ORGS,
        "advisor_name": "Dr. Tricia Shultz",
        "president_name": "Jackson Kress",
        "description": "The goal of the Accounting Society is to expose students "
        "to the professional world and to current issues related to accounting and business. "
        "This is done through various speakers, seminars, and office visits involving professionals "
        "in public and private accounting, banking, and finance. These activities help assist "
        "upperclassmen to make job decisions and help inform underclassmen of the many career opportunities "
        "available to accountants. The Accounting Society is open to students majoring in accounting, "
        "business, finance, and economics." 
    },
    {
        #2
        "club_name": "American Chemical Society",
        "org_type": OrgType.ACADEMIC_PROFESSIONAL_ORGS,
        "advisor_name": "Dr. Susan Cramer",
        "president_name": "Simon Hershberger",
        "description": "As a student affiliate chapter of the American Chemical Society, "
        "the organization encourages advancement in all branches of chemistry. "
        "Internships and graduate school opportunities are made visible through guest speakers, "
        "seminars, and field trips. Open to all students, the society also offers free tutoring to "
        "general and organic chemistry students."
    },
    {
        #3
        "club_name": "American Sign Language Club",
        "abrev": "ASL",
        "org_type": OrgType.ACADEMIC_PROFESSIONAL_ORGS,
        "advisor_name": "TBD",
        "president_name": "Alice Crane",
        "description": "The club's focus is to serve and minister to the deaf and hearing-impaired, "
        "increase the awareness and understanding of those with hearing regarding the deaf and "
        "hearing-impaired community, and seek to foster a greater understanding or interest in "
        "signing in/for worship services."
    },
    {
        #4
        "club_name": "American Society of Heating, Refrigeration, and Air-Conditioning Engineers",
        "abrev": "ASHRAE",
        "org_type": OrgType.ACADEMIC_PROFESSIONAL_ORGS,
        "advisor_name": "Dr. Erik Bardy",
        "president_name": "Jackson Obaugh",
        "description": "The GCC Student Branch of ASHRAE will advance the arts and sciences of "
        "heating, ventilation, air conditioning, and refrigeration, as well as related human "
        "factors, to serve the evolving needs of the public and of ASHRAE. ASHRAE, founded "
        "in 1894, is an international organization of 51,000 members. The GCC Student Branch "
        "provides social and professional networking opportunities for the engineering students "
        "at the college with professionals in the industry of HVAC industry.  This will be "
        "accomplished by attending the monthly meetings of the Pittsburgh chapter of "
        "ASHRAE as well as participating in tours of heating, ventilation, and air-conditioning "
        "systems of area buildings."
    },
    {   
        #5
        "club_name": "American Society of Mechanical Engineers",
        "abrev": "ASME",
        "org_type": OrgType.ACADEMIC_PROFESSIONAL_ORGS,
        "advisor_name": "Dr. Qiuyan Li",
        "president_name": "Hannah Joy",
        "description": "The ASME is the professional organization for mechanical engineers. "
        "The student section at Grove City College strives “to provide an opportunity for "
        "students to begin their professional careers by joining a professional "
        "engineering society; to inform students of recent developments in the field "
        "through publications, field trips, and meetings; to promote fellowship and "
        "interaction with other mechanical engineers.”  Thus, the club sponsors "
        "meetings with speakers from industry and academia, field trips to local companies, "
        "and attendance at conferences, which often have competitions."
    },
    {
        #6
        "club_name": "Association of Computing Machinery",
        "abrev": "ACM",
        "org_type": OrgType.ACADEMIC_PROFESSIONAL_ORGS,
        "advisor_name": "Dr. Jonathan Hutchins",
        "president_name": "John Bauer",
        "description": "The GCC Chapter of the ACM will exist to create a greater "
        "interest in computing and its applications, to be a means of communication "
        "between persons having an interest in computing, and to facilitate career development "
        "by inviting professionals from the business and academic community to advise students "
        "on technical topics and job-related information, including internship and full-time "
        "job opportunities." 
    },
    {
        #7
        "club_name": "Astronomy Club",
        "org_type": OrgType.ACADEMIC_PROFESSIONAL_ORGS,
        "advisor_name": "Dr. James Clem",
        "president_name": "Isabel Paul",
        "description": "The purpose of Astronomy Club is to spread awareness, appreciation, "
        "and awe for God and His universe. We accomplish this by hosting regular "
        "informational meetings and practical stargazing sessions, all while having a "
        "ton of fun as a community."
    },
    {
        #8
        "club_name": "BSW / Social Work Club",
        "org_type": OrgType.ACADEMIC_PROFESSIONAL_ORGS,
        "advisor_name": "Dr. Vannessa Vassar-Bush",
        "president_name": "TBD",
        "description": "The Social Work Club exists to provide support and opportunities "
        "for connection to students in the BSW program, educate the GCC campus community "
        "about social work, and serve the GCC and local community through service "
        "related to BSW studies."
    },
    {
        #9
        "club_name": "Christian Medical and Dental Association",
        "org_type": OrgType.ACADEMIC_PROFESSIONAL_ORGS,
        "advisor_name": "Dr. Lisa Antoscewski",
        "president_name": "Jonalyn Wharry",
        "description": "As the name indicates, students interested in the medical field, "
        "most specifically, dentistry, will find networking with other students and the "
        "Faculty to be of sound benefit as they participate in this campus group. "
    },
    {
        #10
        "club_name": "Council for Exceptional Children",
        "org_type": OrgType.ACADEMIC_PROFESSIONAL_ORGS,
        "advisor_name": "Dr. Tammi Martin",
        "president_name": "Addison Paul",
        "description": "This national organization focuses on the educational needs of "
        "children with particular learning and instructional requirements. It offers "
        "resources that better equip teachers to serve students with special needs."
    },
    {
        #11
        "club_name": "Crimson Collegiate Investors",
        "abrev": "CCI",
        "org_type": OrgType.ACADEMIC_PROFESSIONAL_ORGS,
        "advisor_name": "Dr. Teagan Truitt",
        "president_name": "Ryan Turner",
        "description": "Crimson Collegiate Investors educates members in securities "
        "analysis and investment theory and practice, and provides students with "
        "practical experience in how a fund researches, invests, and generally "
        "functions. Second, CCI promotes ethical investment practice. Finally, "
        "CCI provides networking opportunities to aid students in fulfilling "
        "internship and career aspirations in the field of investment management."
    },
    {
        #12
        "club_name": "Environmental Club",
        "org_type": OrgType.ACADEMIC_PROFESSIONAL_ORGS,
        "advisor_name": "Dr. Darren Wood",
        "president_name": "Lauren Gunning",
        "description": "The Environmental Club is open to all students interested "
        "in working and serving to improve their environment. Projects include "
        "on-campus recycling and other off-campus clean-up projects. They also "
        "work alongside other campus environmental groups. "
    },
    {
        #13
        "club_name": "Exercise Science Club",
        "org_type": OrgType.ACADEMIC_PROFESSIONAL_ORGS,
        "advisor_name": "Dr. Jeffrey Buxton",
        "president_name": "Kiara White",
        "description": "The Exercise Science Club is focused on helping students "
        "within the major of Exercise Science and those not in the major to find "
        "a healthy balance between mind and body. Both the mind and body need "
        "to work as one to get the most out of each exercise routine, healthy "
        "habits. The purpose of the Exercise Science Club is to provide the "
        "Grove City College campus community access to fitness-based education "
        "and activities while preparing competent entry-level Exercise Science "
        "professionals within the Exercise Science major, as well as to "
        "increase awareness of and opportunity for lifelong physical "
        "activity throughout the Grove City College campus community."
    },
    {
        #14
        "club_name": "Federalist Society",
        "org_type": OrgType.ACADEMIC_PROFESSIONAL_ORGS,
        "advisor_name": "Dr. Caleb Verbois",
        "president_name": "Abel Jones",
        "description": "GCC Federalist Society exists to promote intellectual discussion "
        "surrounding our legal order and essential principles upon which it was "
        "founded. These principles include ideas that the state exists to "
        "preserve freedom, that the separation of governmental powers is central "
        "to our Constitution, and that it is emphatically the province and duty "
        "of the judiciary to say what the law is, not what it ought to be. This "
        "entails reordering priorities within the legal system to place a focus "
        "on individual liberty, traditional values, and the rule of law. Our "
        "organization aims to promote these ideas and foster discussion surrounding "
        "their application to our legal realm. We will be an organization of ideas, "
        "not political ideology, so we will present a non-partisan approach encouraging "
        "freedom of thought and expression."
    },
    {
        #15
        "club_name": "French Club",
        "org_type": OrgType.ACADEMIC_PROFESSIONAL_ORGS,
        "advisor_name": "Dr. Kelsey Madsen",
        "president_name": "Ruth Wile",
        "description": "The French Club is composed of students interested in the French "
        "language and culture. Club activities include movies, games, baking, and "
        "trips to French art exhibits, plays, restaurants, and cafés. The organization "
        "strives to promote a deeper appreciation of the peoples and culture of the "
        "francophone world among both club members and the general campus community."
    },
    {
        #16
        "club_name": "Institute of Electrical and Electronic Engineers",
        "abrev": "IEEE",
        "org_type": OrgType.ACADEMIC_PROFESSIONAL_ORGS,
        "advisor_name": "Dr. Luke Rumbaugh",
        "president_name": "Jacob Huber",
        "description": "The Institute of Electrical and Electronics Engineers, Inc. is the "
        "largest professional engineering society in the world. The objective of Grove City's "
        "chapter of the IEEE is scientific, literary, and educational. Its aims include "
        "the advancement of the theory and practice of electrical engineering, electronics, "
        "radio, and allied branches of engineering, as well as related arts and sciences. "
        "It provides students interested in electrical engineering with an opportunity to "
        "gain greater professional insight and experience in their future field."
    },
    {
        #17
        "club_name": "Management Association",
        "org_type": OrgType.ACADEMIC_PROFESSIONAL_ORGS,
        "advisor_name": "Dr. Wayne Biddle",
        "president_name": "Noah Crawford",
        "description": "The Management Association attempts to provide students from various "
        "departmental majors with the opportunity to meet chief executives, businessmen, and "
        "industrial leaders. Interested students may sign up for membership at the Organizational "
        "Fair or at the Association's first meeting."
    },
    {
        #18
        "club_name": "Mathematics Society",
        "org_type": OrgType.ACADEMIC_PROFESSIONAL_ORGS,
        "advisor_name": "Dr. Kelleen Bonomo",
        "president_name": "Jacob Phillips",
        "description": "The purpose of the Mathematics Society is to foster an appreciation "
        "for the study of mathematics and encourage students to engage in mathematical "
        "problem-solving inside and outside the classroom. During biweekly meetings, "
        "we will provide food and drinks, play games related to strategy, puzzles, "
        "and math, and host occasional guest speakers."
    },
    {
        #19
        "club_name": "Nursing Club",
        "org_type": OrgType.ACADEMIC_PROFESSIONAL_ORGS,
        "advisor_name": "Dr. Janet Skees",
        "president_name": "Elizabeth Anderson",
        "description": "The purpose of the Nursing Club is to foster a sense of community "
        "among nursing majors and support them emotionally, spiritually, academically, "
        "and professionally through a healthcare community. The club participates in "
        "weekly meals with members and discussions to facilitate deep, thoughtful, and "
        "growing conversations regarding student nursing struggles through a Christian worldview."
    },
    {
        #20
        "club_name": "Pennsylvania Collegiate Music Educators Association",
        "abrev": "PCMEA",
        "org_type": OrgType.ACADEMIC_PROFESSIONAL_ORGS,
        "advisor_name": "Dr. Jeffrey Tedford",
        "president_name": "Rachel Lewis",
        "description": "The PCMEA student chapter is composed of those students interested "
        "in the teaching of music and the promotion of that profession. This organization "
        "provides, through programs and meetings, a forum for students to engage in "
        "professional activities and discussions with educators relative to music education. "
        "Membership is open to all music majors and all interested in the promotion of the music field."
    },
    {
        #21
        "club_name": "Physics Club",
        "org_type": OrgType.ACADEMIC_PROFESSIONAL_ORGS,
        "advisor_name": "Dr. D.J. Wagner",
        "president_name": "Andrew Vahlberg",
        "description": "The Physics Club, formed in 1962, is designed particularly for students "
        "interested in physics and related sciences. The purpose of the club is to "
        "encourage broader knowledge of physics and an understanding of the field of "
        "physics. Meetings are held once a month and include speakers, movies, and "
        "tours of industrial research centers."
    },
    {
        #22
        "club_name": "Pre-Health Society",
        "org_type": OrgType.ACADEMIC_PROFESSIONAL_ORGS,
        "advisor_name": "Dr. Tracy Farone",
        "president_name": "Martina Stasko",
        "description": "The Pre-Health Society seeks to assist students as they prepare for "
        "admission to professional programs in the health field. The Society aids students "
        "as they explore the health professions, engage in volunteer activities, and "
        "prepare to apply for programs, including, but not limited to, medical "
        "school, nursing school, physical therapy school, veterinary school, and "
        "dentistry school.  Upperclassmen with valuable experience in pre-professional "
        "coursework will offer advice to younger students.  Regular meetings occur "
        "once each month, and various additional opportunities occur throughout each semester."
    },
    {
        #23
        "club_name": "Secondary Education Society",
        "org_type": OrgType.ACADEMIC_PROFESSIONAL_ORGS,
        "advisor_name": "Dr. Nathan Scholten",
        "president_name": "Ryan Metzler",
        "description": "The Secondary Education Society is open to all students studying secondary education."
    },
    {
        #24
        "club_name": "Society of Automotive Engineers/Baja Race Team",
        "abrev": "BAJA",
        "org_type": OrgType.ACADEMIC_PROFESSIONAL_ORGS,
        "advisor_name": "Dr. John Dixon",
        "president_name": "Samuel Brown",
        "description": "The Society of Automotive Engineers/Baja Race Team challenges "
        "engineering students to design and build an off-road vehicle capable of "
        "withstanding the harsh punishment of rough terrain and water. As in real-world "
        "situations, these future engineers work together as a team to resolve technical "
        "challenges in design, test, and manufacturing, as well as business issues. "
        "While our primary focus is SAE-hosted competitions, we also organize our own "
        "race, a great opportunity for members interested in marketing and event planning."
    },
    {
        #25
        "club_name": "Society of Women Engineers",
        "abrev": "SWE",
        "org_type": OrgType.ACADEMIC_PROFESSIONAL_ORGS,
        "advisor_name": "Dr. Michelle Clauss",
        "president_name": "Natalie Krahulik",
        "description": "The Society of Women Engineers is a national organization for "
        "women in engineering and other related sciences. Our students' focus is to "
        "encourage women to achieve their full potential in a career as engineers "
        "and leaders, to lend support to academic pursuits, and to promote "
        "interests in the areas of engineering and the sciences. The activities "
        "of the group include campus and community events such as dinners, "
        "field trips, invited speakers, and visits to senior high school classes. "
        "All women in engineering and the sciences are invited to join."
    },
    {
        #26
        "club_name": "Spanish Club",
        "org_type": OrgType.ACADEMIC_PROFESSIONAL_ORGS,
        "advisor_name": "Dr. Jason Killam",
        "president_name": "Lia Grandi",
        "description": "The Spanish Club is composed of students with an interest "
        "in Hispanic culture. The club participates in activities such as films, "
        "slides, trips, and the Food Fair. This organization strives for a general "
        "appreciation of Spanish culture among language students and the campus as a whole."
    },
    {
        #27
        "club_name": "Speech and Debate Team",
        "org_type": OrgType.ACADEMIC_PROFESSIONAL_ORGS,
        "advisor_name": "Dr. Jason Edwards",
        "president_name": "Ginger Schiffmayer",
        "description": "The GCC Speech and Debate team is an intercollegiate "
        "team that competes at forensics tournaments around the country. Select "
        "students also represent The College at the Pennsylvania State Championship "
        "and the Nationals. Students compete in Parliamentary debate, Platform Events "
        "(oratory), Limited Preparation Events, and Interpretation Events."
    },
    {
        #28
        "club_name": "Startup Club",
        "org_type": OrgType.ACADEMIC_PROFESSIONAL_ORGS,
        "advisor_name": "Mr. Robb Myer",
        "president_name": "Stella Brejwo",
        "description": "Startup Club exists to form networks across different majors, "
        "careers, and build relationships between alumni and current students. Our "
        "focus is helping people understand how to pursue and share their faith in their "
        "profession and expose students to entrepreneurial skills that can be utilized to "
        "help people excel through their careers."
    },
    {
        #29
        "club_name": "Student Chapter of the National Association of Teachers of Singing",
        "abrev": "SNATS",
        "org_type": OrgType.ACADEMIC_PROFESSIONAL_ORGS,
        "advisor_name": "Dr. Katherine Mueller",
        "president_name": "Kassiani Kostos",
        "description": "SNATS provides student members with opportunities for professional "
        "development, such as hearing guest lectures and recitals, exploring current topics "
        "in vocal pedagogy, teaching non-collegiate students in the community under "
        "professor mentorship, and connecting with broader SNATS communities. We encourage "
        "participation in competitions hosted by the National Association of Teachers of Singing."
    },
    {
        #30
        "club_name": "The Wildlife Society",
        "org_type": OrgType.ACADEMIC_PROFESSIONAL_ORGS,
        "advisor_name": "Dr. Darren Wood",
        "president_name": "Grace Chapman",
        "description": "The Wildlife Society is an organization for conservation biology "
        "and non-health biology majors to aid in professional development and career "
        "skills necessary for a successful career in the conservation field. This focus "
        "will be achieved through inviting speakers to campus to discuss various subjects, "
        "such as internships, graduate schools, or career paths. TWS also strives to foster "
        "deep connections between students that will last past college for years to come."
    },
    {
        #31
        "club_name": "Women for Computer Science",
        "abrev": "WFCS",
        "org_type": OrgType.ACADEMIC_PROFESSIONAL_ORGS,
        "advisor_name": "Dr. Jonathan Hutchins",
        "president_name": "Wynonna Roberts",
        "description": "Women for Computer Science is an organization designed to build "
        "community amongst women students in the computer science academic program, assist "
        "in professional development, and aid women in networking in their field."
    },
    {
        #32
       "club_name": "Art & Soul",
        "org_type": OrgType.ARTS_ORGS,
        "advisor_name": "Mr. Glen Sanders",
        "president_name": "TBD",
        "description": "Art & Soul seeks to cultivate a creative community through fine "
        "art-related events for the Grove City College student body. We are dedicated to "
        "teaching our community about how art connects with our spiritual lives and how to "
        "incorporate art into our everyday lives." 
    },
    {
        #33
        "club_name": "Ballroom Dance Club",
        "org_type": OrgType.ARTS_ORGS,
        "advisor_name": "Mr. Kevin Garvey",
        "president_name": "Cole Amacker",
        "description": "The Ballroom Dance Club aims to allow students to learn social "
        "ballroom dancing, get to know other students, and relieve stress." 
    },
    {
        #34
        "club_name": "Fireside Poets",
        "org_type": OrgType.ARTS_ORGS,
        "advisor_name": "Dr. Eric Potter",
        "president_name": "Mary Herman",
        "description": "Fireside Poets is a student-led poetry writing and discussion "
        "group. The club holds weekly meetings in which members appreciate the beauty of "
        "existing poetry and work on honing their skills. All are welcome to attend." 
    },
    {
        #35
        "club_name": "GCC Line Dance Club",
        "org_type": OrgType.ARTS_ORGS,
        "advisor_name": "Dr. Erik Bardy",
        "president_name": "Abigail Cogar",
        "description": "GCC Line Dance Club is a social dance club that teaches "
        "weekly lessons to anyone and everyone willing to learn. Our goal is to "
        "provide an opportunity for students to learn and bring people together by "
        "sharing the gift of dance!" 
    },
    {
        #36
        "club_name": "Swing Dance Club",
        "org_type": OrgType.ARTS_ORGS,
        "advisor_name": "Dr. Erik Bardy",
        "president_name": "Sarah Smith",
        "description": "Swing Dance Club is a social dance club that teaches weekly "
        "lessons to anyone and everyone willing to learn. Our goal is to provide an "
        "opportunity for students to learn and bring people together by sharing the gift of dance!" 
    },
    {
        #37
        "club_name": "Writer's Anonymous",
        "org_type": OrgType.ARTS_ORGS,
        "advisor_name": "Dr. Kimberly Miller",
        "president_name": "Elizabeth Jenkins",
        "description": "Writer's Anonymous is a student-led interest club for aspiring "
        "novelists. They meet weekly to write, troubleshoot ideas and story concepts, "
        "and find community in one another. Their goal is to create a safe space for young "
        "authors to support one another." 
    },
    {
        #38
        "club_name": "College Democrats",
        "org_type": OrgType.POLY_ORGS,
        "advisor_name": "Dr. Erik Anderson",
        "president_name": "Melinda Blum",
        "description": "The purpose of the College Democrats is to offer the Democratic "
        "Party viewpoint on the Grove City College campus and provide a forum for alternative "
        "political viewpoints to be expressed, regardless of ideology. This organization will "
        "attempt to increase awareness of political issues both on the Grove City College "
        "campus and in the surrounding community, promote voter registration, and offer "
        "volunteer support to local Democratic candidates running for political office." 
    },
    {
        #39
        "club_name": "College Republicans",
        "org_type": OrgType.POLY_ORGS,
        "advisor_name": "Dr. Michael Coulter",
        "president_name": "Ewan Maxwell",
        "description": "The Grove City College Republicans works closely with the "
        "Republican Party and Republican organizations across the state to support and "
        "promote the party and to establish a pipeline of voter support for the party as well. "
        "They do this by hosting party events, supporting party campaigns, and advocating on behalf of "
        "the party of colleges throughout the state."
    },
    {
        #40
        "club_name": "Mises Society",
        "org_type": OrgType.POLY_ORGS,
        "advisor_name": "Dr. Shawn Ritenour",
        "president_name": "Dominic Cross",
        "description": "The Mises Society is a student organization following the intellectual tradition "
        "of Ludwig von Mises and Murray N. Rothbard. Its purpose is to promote fellowship among "
        "like-minded students and to engage the college community in discussing the ideas of a free "
        "society, thus upholding the principles of Christendom. More specifically, the group defends and "
        "promotes the ideas of the Austrian School of Economics, property rights, the free market, sound money, and peace."
    },
    {
        #41
        "club_name": "Turning Point USA at Grove City College",
        "abrev": "TPUSA at GCC",
        "org_type": OrgType.POLY_ORGS,
        "advisor_name": "Mr. Keith Graybill",
        "president_name": "Moira Donovan",
        "description": "The purpose of Turning Point USA at Grove City College is to educate and equip students "
        "in the values of fiscal responsibility, free markets, and limited government, promoting the principles "
        "of freedom and individual liberty respectfully and civilly. In all we do, we seek to reflect the character "
        "of Christ--demonstrating truth, humility, and love--by integrating a Christian worldview into our efforts. "
        "This chapter will also host activities that foster civic engagement and encourage open, thoughtful dialogue on campus."
    },
    {
        #42
        "club_name": "Young Americans for Freedom",
        "org_type": OrgType.POLY_ORGS,
        "advisor_name": "TBD",
        "president_name": "Lillian Foos",
        "description": "Young Americans for Freedom provides a community for students to discuss current events and "
        "their relevance to Conservative issues. The club's values align closely with The Sharon Statement, a document "
        "written by young conservatives in 1990 who believed strongly in limited government, the dignity of human life, "
        "free markets, and personal responsibility. Throughout the year, the club participates in various activism "
        "opportunities, including a Pro-Life Timeline, Freedom Week, and the 9/11 Never Forget Project."
    },
    {
        #43
        "club_name": "Young Women for America",
        "abrev": "YWA",
        "org_type": OrgType.POLY_ORGS,
        "advisor_name": "Mrs. Gwen Graybill",
        "president_name": "Maggie Charles",
        "description": "Young Women for America is a community for women who are Christian and politically conservative. "
        "YWA is a chapter of Concerned Women for America and focuses on seven core issues: family, sanctity of life, religious "
        "liberty, education, sexual exploitation, national sovereignty, and support for Israel. YWA allows like-minded women "
        "to politically engage in God-honoring ways and form deep relationships with one another."
    },
    {
        #44
        "club_name": "Cogitare Magazine",
        "org_type": OrgType.PUBLICATION_ORGS,
        "advisor_name": "Dr. Carl Trueman",
        "president_name": "Anastasia Brown",
        "description": "Cogitare Magazine is a student-run publication that seeks to thoughtfully explore the intersection "
        "of religion, culture, and politics through a Judeo-Christian lens."
    },
    {
        #45
        "club_name": "Journal of Law and Public Policy",
        "org_type": OrgType.PUBLICATION_ORGS,
        "advisor_name": "Dr. Caleb Verbois",
        "president_name": "Roan Fair",
        "description": "The Grove City College Journal of Law and Public Policy was organized in the fall of 2009 and "
        "was originally sponsored by the GCC Law Society. The Journal is devoted to the academic discussion of law and public "
        "policy and the pursuit of scholarly research. The unique, close-knit nature of the College's community allows the "
        "Journal to feature the work of undergraduates, faculty, and alumni, together in one publication, which is a national "
        "precedent. Nearly entirely student-managed, the Journal serves as an educational tool for undergraduate students to gain "
        "invaluable experience that will be helpful in graduate school and their future careers. The participation of alumni "
        "and faculty editors and the inclusion of alumni and faculty submissions add credence to the publication, as well as "
        "to the published work of the undergraduate students, and allow for natural mentoring to take place. This blend of education "
        "level and experience, all working toward a single goal, is what makes the Journal truly unique and allows it to serve the "
        "needs of undergraduate students and benefit its readership at large."
    },
    {
        #46
       "club_name": "The Collegian",
        "org_type": OrgType.PUBLICATION_ORGS,
        "advisor_name": "Mr. Nick Hildebrand",
        "president_name": "Emily Fox",
        "description": "The student newspaper, The Collegian, is owned and published by The College. The paper is published "
        "weekly, free of charge, with the purpose of 1) reporting happenings on campus and beyond and 2) teaching students "
        "responsible journalistic practices. It contains sections for news, perspectives, features, entertainment, religion, "
        "and sports. Student editors and staff handle writing, editing, photography, layout, and all other aspects of newspaper "
        "production, except the actual printing."
    },
    {
        #47
        "club_name": "The Echo",
        "org_type": OrgType.PUBLICATION_ORGS,
        "advisor_name": "Dr. Anne Shepherd",
        "president_name": "Kinley Bowers",
        "description": "The Echo is a student-produced creative review, which features student poetry, prose, fiction, "
        "photography, and artwork. The magazine is published during the Spring semester. Students are urged to submit works "
        "to the magazine or join the various committees involved in producing The Echo."
    },
    {
        #48
        "club_name": "Association for Women Students",
        "abrev": "AWS",
        "org_type": OrgType.SERVICE_ORGS,
        "advisor_name": "Ms. Hannah Kincer",
        "president_name": "Mary God",
        "description": "By hosting fun and exciting events on campus, AWS hopes to nurture community and create engagement for "
        "the women of Grove City College. All female students may request to join the AWS membership. AWS also oversees a "
        "community service program called 'Adopt-a-Grandparent,' which is open to all students on campus."
    },
    {
        #49
       "club_name": "Giving to Grove",
        "org_type": OrgType.SERVICE_ORGS,
        "advisor_name": "Ms. Virginia West",
        "president_name": "Hannah Leeman",
        "description": "Giving to Grove is a community service club that works with and volunteers at local Grove City "
        "nonprofits and organizations. The purpose of the organization is to provide volunteer opportunities to students who "
        "can contribute their time towards supporting the local community. Within the club, there are multiple leadership positions "
        "and various opportunities to join acts of service for those in need."
    },
    {
        #50
        "club_name": "Men's Activities Board",
        "abrev": "MAB",
        "org_type": OrgType.SERVICE_ORGS,
        "advisor_name": "Mr. Isaac Cooke",
        "president_name": "Nathan Devlin",
        "description": "Men's Activities Board functions to establish harmonious living conditions among the male "
        "student body and to assist in the funding of community-engagement events open to all male students. "
        "Meetings are open to all interested Grove City College men."
    },
    {
        #51
        "club_name": "Signature",
        "org_type": OrgType.SERVICE_ORGS,
        "advisor_name": "Dr. Stacy Paparone",
        "president_name": "Grace Mayville",
        "description": "Signature is a group of Christian women who are committed to serving the Fine Arts "
        "Department of Grove City College, as well as the community and the world. Through friendship and fellowship, "
        "we encourage each other to grow and serve in the name of our Lord.  Signature serves at senior recitals, "
        "ushers at music performances, sends encouragement notes to performers, and performs other service activities."
    },
    {
        #52
        "club_name": "Amateur Radio Club",
        "org_type": OrgType.SPECIAL_INTEREST_ORGS,
        "advisor_name": "Dr. James Brooks",
        "president_name": "Joshua Lee",
        "description": "The Grove City College Amateur Radio Club's mission is to promote radio knowledge and the art "
        "of wireless communications. Operating from an FCC-licensed station, the group seeks to teach members about the "
        "different facets of telecommunications as well as provide emergency communications to the campus."
    },
    {
        #53
        "club_name": "Chess Club",
        "org_type": OrgType.SPECIAL_INTEREST_ORGS,
        "advisor_name": "Mr. Timothy Sweet",
        "president_name": "Quinn MacKenzie",
        "description": "If you enjoy the tactics and strategy of one of the greatest games conceived, then the Chess Club is for you."
    },
    {
        #54
        "club_name": "Coffee Culture Club",
        "org_type": OrgType.SPECIAL_INTEREST_ORGS,
        "advisor_name": "Dr. Eric Fehr",
        "president_name": "Ada Vandergoot",
        "description": "Coffee Culture Club is a community centered on fellowship, connection, and a shared appreciation "
        "for one of the world's most beloved beverages: coffee. Beyond the cup, the production, trade, and marketing of "
        "coffee have significant social, cultural, economic, and environmental impacts around the world. The Coffee "
        "Culture Club seeks to foster a deeper understanding and appreciation of coffee by exploring its rich history and "
        "global influence while creating opportunities for fellowship, learning, and meaningful connections over a great "
        "cup of coffee."
    },
    {
        #55
        "club_name": "Commuter Student Association",
        "abrev": "CSA",
        "org_type": OrgType.SPECIAL_INTEREST_ORGS,
        "advisor_name": "Dr. Eric Fehr",
        "president_name": "Anjali Kalsani",
        "description": "The Commuter Student Association (CSA) exists to support and connect commuter students in their "
        "pursuit of personal growth, community, and academic excellence. Through events, resources, and advocacy, CSA is "
        "there to foster a Christ-centered community and aid commuter students in finding ways to engage in the College "
        "community. By building this community, CSA strives to make the commuting experience at Grove City College less "
        "stressful and isolated."
    },
    {
        #56
        "club_name": "Crimsonprov",
        "org_type": OrgType.SPECIAL_INTEREST_ORGS,
        "advisor_name": "Mr. Jonathan Bucci",
        "president_name": "Ben Smith",
        "description": "Crimsonprov is a sketch/improvisation comedy group that teaches students how to build comedy "
        "sketches from scratch in front of a live audience, develop those skills, and perform these sketches live on campus "
        "for the Grove City community."
    },
    {
        #57
        "club_name": "GCC Urban Gaming Club",
        "org_type": OrgType.SPECIAL_INTEREST_ORGS,
        "advisor_name": "Dr. Brian Dellinger",
        "president_name": "Sophia Bowers",
        "description": "The Urban Gaming Club is a fun, low-commitment alternative to traditional sports. Activities of the "
        "Urban Gaming Club consist of Nerf Human vs. Zombies, Nerf PVP, and LARP. meetings take place on Tuesday evenings, "
        "normally, and are never mandatory."
    },
    {
        #58
        "club_name": "Grove City Socratic Club",
        "org_type": OrgType.SPECIAL_INTEREST_ORGS,
        "advisor_name": "Dr. Ryan West",
        "president_name": "Brae Sadler",
        "description": "The Grove City Socratic Club, in the spirit of C.S. Lewis' Oxford Socratic Club, engages in "
        "table discussions about controversial topics, chiefly theological, within Christianity. Members have constructive "
        "discussions engaging with each other's beliefs about a specific doctrine and defense of that belief, pursuing the "
        "truth in life; for God is Truth, and God is love."
    },
    {
        #59
        "club_name": "His Power Displayed",
        "org_type": OrgType.SPECIAL_INTEREST_ORGS,
        "advisor_name": "Dr. Matthew Vogel",
        "president_name": "TBD",
        "description": "The mission of His Power DISplayed (HPD) is to create a community for disabled and able-bodied "
        "students to explore what it means to be a disabled Christian student. We also want to learn how to best support and "
        "advocate for each other."
    },
    {
        #60
       "club_name": "ISI at Grove City College: The Fugitives",
        "abrev": "Fugitives",
        "org_type": OrgType.SPECIAL_INTEREST_ORGS,
        "advisor_name": "Dr. Jason Edwards",
        "president_name": "John Hatzis",
        "description": "The Fugitives is an organization that stands upon the Agrarian tradition.  The Fugitives seeks to "
        "provide a unique context in which Grove City College students will meet outside of the classroom to further their "
        "educations, develop their worldviews, and apply their beliefs through action to the world around them.  The group "
        "furthers its purpose through a variety of activities, with an emphasis on the discussion and critical analysis of "
        "various authors' works. On occasion, Intercollegiate Studies Institute materials are used." 
    },
    {
        #61
        "club_name": "Lux Mea",
        "org_type": OrgType.SPECIAL_INTEREST_ORGS,
        "advisor_name": "Dr. Andrew Mitchell",
        "president_name": "Maya O'Dell"
    },
    {
        #62
       "club_name": "MuKappa",
        "abrev": "MK",
        "org_type": OrgType.SPECIAL_INTEREST_ORGS,
        "advisor_name": "Ms. Chloe Wilhelm",
        "president_name": "David Frerichs",
        "description": "MuKappa seeks to assist students who have grown up in an international context to transition "
        "well to Grove City by cultivating Christ-centered relationships with other students and equipping them to fully "
        "engage with the mission of Grove City College. Events are held monthly and are open to any interested Grove City College student." 
    },
    {
        #63
        "club_name": "Pan-Asian Association",
        "org_type": OrgType.SPECIAL_INTEREST_ORGS,
        "advisor_name": "Dr. Seulgi Byun",
        "president_name": "Abigail Collier",
        "description": "The Pan-Asian Association focuses on all things Chinese, from language, culture, and society to "
        "art, literature, and food. As China’s global stand broadens and its influence increases, all students are welcome to "
        "enjoy a deeper investigation of the legendary Middle Kingdom with the Pan-Asian Association."
    },
    {
        #64
        "club_name": "Philsophy Society",
        "org_type": OrgType.SPECIAL_INTEREST_ORGS,
        "advisor_name": "Dr. Christopher Franklin",
        "president_name": "TBD"
    },
    {
        #65
        "club_name": "Sola Veritas",
        "org_type": OrgType.SPECIAL_INTEREST_ORGS,
        "advisor_name": "TBD",
        "president_name": "Eli Wick",
        "description": "Sola Veritas is a campus club dedicated to the pursuit of truth and responsible debate. Each Wednesday, "
        "the group examines the theory behind clear, concise argumentation and explores the American history that helps ground "
        "those skills. The club includes students from a wide range of political perspectives; all committed to supporting "
        "others as they develop their own."
    },
    {
        #66
        "club_name": "Survivor Club",
        "org_type": OrgType.SPECIAL_INTEREST_ORGS,
        "advisor_name": "Dr. John Smith",
        "president_name": "Weston McGregor",
        "description": "Survivor Club is a special interest club surrounding the CBS Reality TV series, Survivor. For 44 seasons, "
        "Survivor has thrilled its viewers with the ultimate social experiment. Survivor Club is for all familiarities, whether "
        "brand new or die-hard superfan. Contact the president to learn about joining the group to watch the show and even "
        "participate in GCC's very own version of Survivor on Campus!"
    },
    {
        #67
        "club_name": "The Order of St. George",
        "abrev": "OSG",
        "org_type": OrgType.SPECIAL_INTEREST_ORGS,
        "advisor_name": "Dr. Brian Dellinger",
        "president_name": "Joshua Johnson",
        "description": "The Order of St. George (OSG) is an on-campus society of individuals whose activities include weekly "
        "meetings, board game nights, anime watch parties, movie nights, D&D/tabletop RPG one-shots, and Super Smash Bros "
        "Ultimate weekly brackets. The OSG encourages its members to embrace their creativity, create long-lasting friendships, "
        "and enjoy the many aspects of popular culture of the past and present. The profits made from the numerous OSG events are "
        "donated to Extra Life."
    },
    {
        #68
       "club_name": "Wolverine Broadcast Network",
        "abrev": "WBN",
        "org_type": OrgType.SPECIAL_INTEREST_ORGS,
        "advisor_name": "Dr. Vince DiStasi",
        "president_name": "Molly Miller",
        "description": "Through broadcasting excellence centered around the truth of Jesus Christ, the Wolverine Broadcast Network "
        "seeks to glorify God by entertaining, informing, and inspiring listeners both locally and beyond with strong campus "
        "engagement, innovative technology, and student creativity while professionally developing the next generation of "
        "broadcasting talent. This is a web-based platform."
    },
    {
        #69
        "club_name": "GCC Disc Golf Club",
        "org_type": OrgType.RECREATION_ORGS,
        "advisor_name": "Dr. Jason Killam",
        "president_name": "Andrew Castner",
        "description": "For competitive and social players, GCC Disc Golf aims to provide opportunities for students to "
        "engage in the sport of Disc Golf and compete in local and intercollegiate competitions."
    },
    {
        #70
        "club_name": "Grove City College Fly Fishing Club",
        "org_type": OrgType.RECREATION_ORGS,
        "advisor_name": "Dr. Donald Shepson",
        "president_name": "Elena Kennedy",
        "description": "The Grove City College Fly Fishing Club looks to cultivate a community centered on fly fishing and "
        "stewardship of one another. This group embraces everyone from highly skilled anglers to those with no experience "
        "at all. Club activities include fly-fishing, fly-tying classes, monthly meetings, and more!"
    },
    {
        #71
        "club_name": "Men's Wrestling Club",
        "org_type": OrgType.RECREATION_ORGS,
        "advisor_name": "Mr. Cedric Lewis",
        "president_name": "Dallas Casciani",
        "description": "The Grove City College Men's Wrestling Club is a student-led athletic organization dedicated "
        "to promoting the sport of wrestling, physical fitness, and character development within a Christ-centered "
        "community. The club provides Grove City College students with opportunities to train, compete in intercollegiate "
        "matches, and grow as leaders both on and off the mat. Through disciplined practices, teamwork, and service, "
        "the GCC Men's Wrestling Club strives to build a culture of excellence, integrity, and brotherhood that "
        "reflects the College's mission and values."
    },
    {
        #72
        "club_name": "Outing Club",
        "org_type": OrgType.RECREATION_ORGS,
        "advisor_name": "Dr. Devin Stauff",
        "president_name": "Connor Stoltzfus",
        "description": "The Outing Club sponsors a variety of outdoor activities that occur weekly. Activities "
        "include camping, biking, a pig roast, and trips to the alumni cabin in the Pennsylvania forest. Any special "
        "activities sponsored by the club must have the approval, in advance, of the Vice President for Student "
        "Life and Learning."
    },
    {
        #73
        "club_name": "Delight Ministries",
        "org_type": OrgType.MINISTRY_ORGS,
        "advisor_name": "Ms. Carrie Leisher",
        "president_name": "Gabrielle Farcas",
        "description": "This group is for Christian women to find a community with other Christian women. We meet for "
        "weekly Bible studies, group activities, worship, and much more with a focus on vulnerability, accountability, and community."
    },
    {
        #74
        "club_name": "Engineers with a Mission",
        "org_type": OrgType.MINISTRY_ORGS,
        "advisor_name": "Dr. Erik Bardy",
        "president_name": "Andrew Castner",
        "description": "Engineers with a Mission is a student-led club comprised of engineering majors and more. Our "
        "mission is to be the hands and feet of Christ by helping communities around the world develop the ability to "
        "maintain their basic human needs sustainably."
    },
    {
        #75
        "club_name": "Fellowship of Christian Athletes",
        "abrev": "FCA",
        "org_type": OrgType.MINISTRY_ORGS,
        "advisor_name": "Mr. Tim Forry",
        "president_name": "Josh McDermott",
        "description": "This group is open to men and women athletes and to those interested in athletics who have a "
        "Christian perspective of play and competition. The national purpose of FCA is to confront athletes and "
        "coaches with the challenges and adventures of following Christ. Meetings are held on Sunday evenings "
        "and include singing, discussion, Bible study, and/or athletics."
    },
    {
        #76
        "club_name": "Fellowship of Christian Educators",
        "abrev": "FCE",
        "org_type": OrgType.MINISTRY_ORGS,
        "advisor_name": "Dr. Jarrett Chapman",
        "president_name": "Jessica Eisenhart",
        "description": "The purpose of this organization is to encourage Grove City College students to "
        "seek a Christian perspective in education and to provide an opportunity for those students to develop "
        "an understanding of Christian principles and ideas within this context. The FCE provides a service "
        "for those interested in expanding their awareness of the place, function, and result of Christianity in the classroom."
    },
    {
        #77
        "club_name": "Hymn Sing",
        "org_type": OrgType.MINISTRY_ORGS,
        "advisor_name": "Dr. Paul Munson",
        "president_name": "June Lee",
        "description": "Hymn Sing seeks to provide students with a community in which they may participate in "
        "the weekly singing of hymns. Outside of regular meetings, the group may be found hosting English Country "
        "Line Dances and engaging in weekly meals."
    },
    {
        #78
       "club_name": "International Justice Mission",
        "abrev": "IJM",
        "org_type": OrgType.MINISTRY_ORGS,
        "advisor_name": "Dr. Donald Shepson",
        "president_name": "Ana Monroe",
        "description": "The International Justice Mission [IJM] is dedicated to the Christian purpose of advancing "
        "the Scriptural mandate to help people suffering injustice and oppression who cannot rely on local authorities "
        "for relief. IJM informs and educates others regarding these injustices. IJM brings to light human rights violations "
        "and supports [monetarily] lawyers who support victims and the enforcement of those corrected injustices." 
    },
    {
        #79
        "club_name": "Koinonia Gospel Team",
        "abrev": "KGT",
        "org_type": OrgType.MINISTRY_ORGS,
        "advisor_name": "Dr. James Bibza & Dr. Eric Bancroft",
        "president_name": "Sabrina Harrison",
        "description": "Koinonia, a Greek word meaning intimate fellowship, is the idea on which this group is based. "
        "Celebrating the good news, the group meets twice a week to sing, study the Bible, and prepare worship "
        "services for the community. The Gospel Team travels to local and distant churches to lead congregations in "
        "worship through song, prayer, and the spoken word. The Gospel team meets on Monday evenings for practice and a "
        "time of fellowship. Meetings on Wednesdays are for Bible studies, praise, and prayer. Membership is open to anyone "
        "willing to commit to the ministry."
    },
    {
        #80
        "club_name": "Life Advocates",
        "org_type": OrgType.MINISTRY_ORGS,
        "advisor_name": "Dr. Dale McIntyre",
        "president_name": "Kiara Frey",
        "description": "The Life Advocates is a non-denominational group bound by their convictions concerning the "
        "Biblical truths concerning the issues of abortion, infanticide, and euthanasia. They believe that the value of "
        "human life is an issue of universal public concern and not merely a matter of personal morality. Their purpose "
        "is to inform the college community about local and national issues concerned with the value of human life. Meetings are bi-monthly."
    },
    {
        #81
        "club_name": "Lutheran Student Fellowship",
        "org_type": OrgType.MINISTRY_ORGS,
        "advisor_name": "Dr. Kelsey Madsen",
        "president_name": "Matthew Purucker",
        "description": "Lutheran Student Fellowship gathers Lutheran students on campus around Bible studies, "
        "doctrinal discussions, and other spiritually enriching activities. Opportunities are available for all "
        "students to explore the Lutheran tradition of the Christian faith, as taught by the Lutheran Church—Missouri Synod (LCMS)."
    },
    {
        #82
        "club_name": "MetbyLove",
        "abrev": "MBL",
        "org_type": OrgType.MINISTRY_ORGS,
        "advisor_name": "Mrs. Victoria Wright",
        "president_name": "Brayden Shrieber",
        "description": "MetbyLove is a campus community that meets for weekly worship and prayer and lives on "
        "mission through weekly evangelism. The purpose of MBL is to see the students at Grove City College 'met' "
        "and 'sent' by the love of Jesus as we pursue Him together. All are welcome!"
    },
    {
        #83
        "club_name": "New Life",
        "org_type": OrgType.MINISTRY_ORGS,
        "advisor_name": "Dr. Martin Bright",
        "president_name": "Pax Robinson",
        "description": "Members of this outreach offer hope and a chance for new life to the young men at a "
        "local juvenile delinquency placement center, George Junior Republic. New Life members can participate "
        "in Thursday evening youth meetings, individual cottage Bible studies, various chapel services, and on-campus "
        "prayer teams. Special events also occur throughout the year."
    },
    {
        #84
        "club_name": "Newman Club",
        "org_type": OrgType.MINISTRY_ORGS,
        "advisor_name": "Dr. James Clem",
        "president_name": "Matt Fittro",
        "description": "The Newman Club is a fellowship organization that seeks to meet the needs of Catholic "
        "students on campus and to educate all interested students about the Catholic faith. The goals of the "
        "group are Christian fellowship. intellectual and spiritual edification, and community service. All students "
        "may participate in any of the activities, which are announced in the weekly newsletter."
    },
    {
        #85
        "club_name": "Orthodox Christian Fellowship",
        "abrev": "OCF",
        "org_type": OrgType.MINISTRY_ORGS,
        "advisor_name": "Dr. Andrew Harvey",
        "president_name": "Sophie Hahn",
        "description": "The Orthodox Christian Fellowship (OCF) is comprised of students who are associated with "
        "the Eastern Orthodox Church and its traditions. All students are welcome to participate in this group's "
        "activities and support their mission on campus."
    },
    {
        #86
        "club_name": "Prison Ministry",
        "org_type": OrgType.MINISTRY_ORGS,
        "advisor_name": "Dr. W. Matt Henderson",
        "president_name": "Samuel Belmonte",
        "description": "Prison Ministry is the campus branch of the National Prison Ministry Fellowship. "
        "The ministry's focus is to pray with and for those in the local Mercer jail. As well as to support "
        "the children of those who find themselves in jail."
    },
    {
        #87
        "club_name": "Ratio Christi",
        "org_type": OrgType.MINISTRY_ORGS,
        "advisor_name": "Dr. Christopher Ansberry",
        "president_name": "Lachlan Campbell",
        "description": "From Augustine to Reinhold Niebuhr, Soren Kierkegaard to Karl Barth, the ideas of "
        "scholars, the Word of God - Investigate how the two have intersected throughout history, and how they "
        "have defended the Christian faith."
    },
    {
        #88
        "club_name": "Simple Charity",
        "org_type": OrgType.MINISTRY_ORGS,
        "advisor_name": "Mr. Thomas Biro",
        "president_name": "Carolyn Stum",
        "description": "The mission of Simple Charity is to help students grow in loving and serving "
        "those in need through studying Jesus' love together and then applying it to our lives through local "
        "service projects and fundraisers."
    },
    {
        #89
        "club_name": "Student Mission Fellowship",
        "org_type": OrgType.MINISTRY_ORGS,
        "advisor_name": "Mr. Thomas Biro",
        "president_name": "Josh Youngquist",
        "description": "This campus group focuses on prayer (praying) for the nations of the world, generally and specifically."
    },
    {
        #90
        "club_name": "Treasured Connections",
        "org_type": OrgType.MINISTRY_ORGS,
        "advisor_name": "Mr. Thomas Biro",
        "president_name": "Sophia Bowers",
        "description": "Treasured Connections is a ministry on campus that serves adults with intellectual "
        "and developmental disabilities by visiting group homes and nursing homes in the area and bringing the "
        "love of God to them. Treasured Connections strives to foster lasting connections with the residents and "
        "staff of these homes through group-facilitated events and activities."
    },
    {
        #91
        "club_name": "Warriors for Christ",
        "abrev": "Warriors",
        "org_type": OrgType.MINISTRY_ORGS,
        "advisor_name": "Mr. Daniel Snoke",
        "president_name": "Chloe Covil",
        "description": "Warriors for Christ, as a group of committed Christians, strive to be used in ushering in "
        "God's Spirit of revival on campus. Their goal is pursued through a meeting time of praise, corporate prayer, "
        "and teaching. Outside of the meeting, small prayer groups are organized for a time of sharing personal "
        "concerns, along with praying for the needs of the campus."
    },
    {
        #92
        "club_name": "Women of Faith",
        "org_type": OrgType.MINISTRY_ORGS,
        "advisor_name": "Ms. Jessica Gayer",
        "president_name": "Jenna Williams",
        "description": "Women of Faith are Grove City College women who seek to meet and worship together as they "
        "grow in their commitment to Christ Jesus."
    },
    {
        #93
        "club_name": "Young Life",
        "abrev": "YL",
        "org_type": OrgType.MINISTRY_ORGS,
        "advisor_name": "Dr. Susan Dreves",
        "president_name": "Luke Demember",
        "description": "Young Life is an international evangelical organization with the primary goal of presenting "
        "Christianity to high school students. This is accomplished by building personal relationships, weekly meetings "
        "(called “Club”), and taking the high school students to Young Life Summer camps. Responsibilities of a Young Life leader "
        "are Club, Campaigners (Bible study for students), and contact work at the high school. Leaders also meet "
        "weekly for a time of fellowship, worship, and prayer."
    },
    {
        #94
        "club_name": "Fencing (COED)",
        "org_type": OrgType.CLUB_SPORT_ORGS,
        "advisor_name": "Mr. Ian Harris",
        "president_name": "Rebecca Froyd",
        "description": "The Grove City Fencing Club provides an opportunity for students to learn classical foil fencing "
        "and to compete against other members of the club. This group exists to enrich its members and spur them to "
        "excellence in their lives and academics through the training and teaching of fencing skills. No previous fencing "
        "experience is required."
    },
    {
        #95
        "club_name": "GCC Martial Arts Club",
        "abrev": "",
        "org_type": OrgType.CLUB_SPORT_ORGS,
        "advisor_name": "Dr. Jeffrey Buxton",
        "president_name": "Wynonna Roberts",
        "description": "The GCC Martial Arts Club focuses its teachings on traditional Tae Kwon-Do/kickboxing, Brazilian "
        "Jiu-Jitsu, and Judo. Classes are optional/pick-and-choose and offered on weekdays to students of all experience "
        "levels, backgrounds, and abilities. The club places a strong focus on mental and physical discipline, self-defense, "
        "and confidence growth."
    },
    {
        #96
        "club_name": "Grove City College Club Ultimate Frisbee (COED)",
        "org_type": OrgType.CLUB_SPORT_ORGS,
        "advisor_name": "Mr. Isaac Cooke",
        "president_name": "James Laird",
        "description": "This co-ed group of intramural athletes is competitive, fun, and a great way to bust the stress "
        "of academic life."
    },
    {
        #97
        "club_name": "Ice Hockey (COED)",
        "org_type": OrgType.CLUB_SPORT_ORGS,
        "advisor_name": "Mr. Luke Tingley",
        "president_name": "Josh Elverson",
        "description": "The ice hockey team is a non-varsity, competitive ice hockey team. Tryouts are held in September "
        "and the season runs from October to March. Games are played locally at Hess Ice Rink in New Castle."
    },
    {
        #98
        "club_name": "Men's Rugby",
        "org_type": OrgType.CLUB_SPORT_ORGS,
        "advisor_name": "Dr. Charles Kriley",
        "president_name": "Trevor Olson",
        "description": "This organization combines great sportsmanship along with strong camaraderie to develop an "
        "outstanding athletic repertoire. The rugby club strives to be a completely self-sufficient model collegiate "
        "rugby club that promotes the positive aspects of the sport of rugby. The rugby club also upholds the values and "
        "ideals of Grove City College."
    },
    {
        #99
        "club_name": "Women's Field Hockey",
        "org_type": OrgType.CLUB_SPORT_ORGS,
        "advisor_name": "Mrs. Tori Wright",
        "president_name": "Bayleigh Miller",
        "description": "With many of our ladies coming from high schools that have Field Hockey as a woman's varsity "
        "sport there is a strong core of women that make up a competitive team of field hockey enthusiasts."
    }

]

