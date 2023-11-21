#REGULAR EXPRESSION PRACTICE
"""
useful website link for regEX pattern checking

https://regex101.com/ 


"""

import re
# text="""
# companies owner phone number is 
# 233345545

# Tesla2s CFO # (999)-333-777

# call him if you have any questions
# """

# patterns='\(\d{3}\)-\d{3}-\d{3}|\d{9}'

# matches=re.findall(patterns,text)
# print(matches)
# result===> (999)-333-777  233345545


# TEXT EXAMPLE 2

text2="""
Tesla, Inc.
Notes to Consolidated Financial Statements
(unaudited)
Note 1 – Overview
Tesla, Inc. (“Tesla”, the “Company”, “we”, “us” or “our”) was incorporated in the State of Delaware on July 1, 2003. We design, develop,
manufacture and sell high-performance fully electric vehicles and design, manufacture, install and sell solar energy generation and energy storage
products. Our Chief Executive Officer, as the chief operating decision maker (“CODM”), organizes our company, manages resource allocations and
measures performance among two operating and reportable segments: (i) automotive and (ii) energy generation and storage.
There continues to be widespread impact from the COVID-19 pandemic. Beginning in the first quarter of 2021, there has been a trend in many
parts of the world of increasing availability and administration of vaccines against COVID-19, as well as an easing of restrictions on social, business,
travel and government activities and functions. On the other hand, infection rates and regulations continue to fluctuate in various regions and there are
ongoing global impacts resulting from the pandemic, including challenges and increases in costs for logistics and supply chains, such as increased port
congestion, intermittent supplier delays and a shortfall of semiconductor supply. We have been affected by temporary manufacturing closures,
employment and compensation adjustments and impediments to administrative activities supporting our product deliveries and deployments.
In addition, we have experienced and are experiencing varying levels of inflation resulting in part from various supply chain disruptions,
increased shipping and transportation costs, increased raw material and labor costs and other disruptions caused by the COVID‐19 pandemic and
general global economic conditions. The inflationary impact on our cost structure has contributed to adjustments in our product pricing, despite a
continued focus on reducing our manufacturing costs where possible.
Note 2 – Summary of Significant Accounting Policies
Unaudited Interim Financial Statements
The consolidated balance sheet as of June 30, 2022, the consolidated statements of operations, the consolidated statements of comprehensive
income, the consolidated statements of redeemable noncontrolling interests and equity for the three and six months ended June 30, 2022 and 2021 and
the consolidated statements of cash flows for the six months ended June 30, 2022 and 2021, as well as other information disclosed in the accompanying
notes, are unaudited. The consolidated balance sheet as of December 31, 2021 was derived from the audited consolidated financial statements as of that
date. The interim consolidated financial statements and the accompanying notes should be read in conjunction with the annual consolidated financial
statements and the accompanying notes contained in our Annual Report on Form 10-K for the year ended December 31, 2021.
The interim consolidated financial statements and the accompanying notes have been prepared on the same basis as the annual consolidated
financial statements and, in the opinion of management, reflect all adjustments, which include only normal recurring adjustments, necessary for a fair
statement of the results of operations for the periods presented. The consolidated results of operations for any interim period are not necessarily
indicative of the results to be expected for the full year or for any other future years or interim periods.

"""

patterns2='Note \d \S ([^\n]+)'

matches2=re.findall(patterns2,text2)
print(matches2)

# result ===> ['Overview', 'Summary of Significant Accounting Policies']

# text3="""
# For example, financial year 2024 is the 12-month 
# period ending on 30 June 2024 and can be referred to as FY2023 Q1
# FY2024 Q4 but leadds to FY2025 Q5.

# """

# patterns3='FY\d{4} Q[1-4]'

# matches23=re.findall(patterns3,text3)

# print(matches23)


# text_Dollar="""For example, financial year 2024 is the 12-month 
# period ending on 30 June 2024 and can be $4.5666 billion referred to as FY2023 Q1
# FY2024 Q4 but leadds to FY2025 Q5 be $2.7 billion."""
# patt='\$[0-9\.]*'

# doll=re.findall(patt,text_Dollar)
# print(doll)


tweet='''



Follow our leader Elon musk on twitter here: https://twitter.com/elonmusk, more information 
on Tesla's products can be found at https://www.tesla.com/. Also here are leading influencers 
for tesla related news,
https://twitter.com/teslarati
https://twitter.com/dummy_tesla
https://twitter.com/dummy_2_tesla
'''



patterns='https:\S\Stwitter.com\S([a-z|A-Z|1-9|_)]+)'

matches=re.findall(patterns,tweet)
print(matches)

types= '''
Concentration of Risk: Credit Risk
Financial instruments that potentially subject us to a concentration of credit risk consist of cash, cash equivalents, marketable securities,
restricted cash, accounts receivable, convertible note hedges, and interest rate swaps. Our cash balances are primarily invested in money market funds
or on deposit at high credit quality financial institutions in the U.S. These deposits are typically in excess of insured limits. As of September 30, 2021
and December 31, 2020, no entity represented 10% or more of our total accounts receivable balance. The risk of concentration for our convertible note
hedges and interest rate swaps is mitigated by transacting with several highly-rated multinational banks.
Concentration of Risk: Supply Risk
We are dependent on our suppliers, including single source suppliers, and the inability of these suppliers to deliver necessary components of our
products in a timely manner at prices, quality levels and volumes acceptable to us, or our inability to efficiently manage these components from these
suppliers, could have a material adverse effect on our business, prospects, financial condition and operating results.
'''

types_pattern='Concentration of Risk: ([A-Z|a-z  |1-9]*)'

types_matches=re.findall(types_pattern,types)
print(types_matches)
