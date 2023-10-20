import random

all_flags = [['ï»¿Aruba', 'Oranjestad', 'AA', 'AA-flag.gif'], ['Antigua and Barbuda', "St. John's", 'AC', 'AC-flag.gif'], ['Andorra', 'Andorra la Vella', 'AD', 'AD-flag.gif'], ['United Arab Emirates', 'Abu Dhabi', 'AE', 'AE-flag.gif'], ['Afghanistan', 'Kabul', 'AF', 'AF-flag.gif'], ['Albania', 'Tirana', 'AL', 'AL-flag.gif'], ['Armenia', 'Yerevan', 'AM', 'AM-flag.gif'], ['Angola', 'Luanda', 'AO', 'AO-flag.gif'], ['Argentina', 'Buenos Aires', 'AR', 'AR-flag.gif'], ['American Samoa', 
'Pago Pago', 'AS', 'AS-flag.gif'], ['Austria', 'Vienna', 'AT', 'AT-flag.gif'], ['Australia', 'Canberra', 'AU', 'AU-flag.gif'], ['Anguilla', 'The Valley', 'AV', 'AV-flag.gif'], ['Azerbaijan', 'Baku', 'AZ', 'AZ-flag.gif'], ['Bosnia and Herzegovina', 'Sarajevo', 'BA', 'BA-flag.gif'], ['Barbados', 'Bridgetown', 'BB', 'BB-flag.gif'], ['Bangladesh', 'Dhaka', 'BD', 'BD-flag.gif'], ['Belgium', 'Brussels', 'BE', 'BE-flag.gif'], ['Burkina Faso', 'Ouagadougou', 'BF', 'BF-flag.gif'], ['Bulgaria', 'Sofia', 'BG', 'BG-flag.gif'], ['Bahrain', 'Manama', 'BH', 'BH-flag.gif'], ['Burundi', 'Bujumbura', 'BI', 'BI-flag.gif'], ['Benin', 'Porto Novo', 'BJ', 'BJ-flag.gif'], ['Bermuda', 'Hamilton', 'BM', 'BM-flag.gif'], ['Brunei', 'Bandar Seri Begawan', 'BN', 'BN-flag.gif'], ['Bolivia', 'Sucre', 'BO', 'BO-flag.gif'], ['Brazil', 'Brasilia', 'BR', 'BR-flag.gif'], ['Bahamas', 'Nassau', 'BS', 'BS-flag.gif'], ['Bhutan', 'Thimphu', 'BT', 'BT-flag.gif'], ['Botswana', 'Gaborone', 'BW', 'BW-flag.gif'], ['Belarus', 'Minsk', 'BY', 'BY-flag.gif'], ['Belize', 'Belmopan', 'BZ', 'BZ-flag.gif'], ['Canada', 'Ottawa', 'CA', 'CA-flag.gif'], ['Democratic Republic of Congo', 'Kinshasa', 'CD', 'CD-flag.gif'], ['Central African Republic', 'Bangui', 'CF', 'CF-flag.gif'], ['Republic of the Congo', 'Brazzaville', 'CG', 'CG-flag.gif'], ['Switzerland', 'Bern', 'CH', 'CH-flag.gif'], ['Ivory Coast', 'Yamoussoukro', 'CI', 'CI-flag.gif'], ['Chile', 'Santiago', 'CL', 'CL-flag.gif'], ['Cameroon', 'YaoundÃ©', 'CM', 'CM-flag.gif'], ['China', 'Beijing', 'CN', 'CN-flag.gif'], ['Colombia', 'Bogota', 'CO', 'CO-flag.gif'], ['Costa Rica', 'San JosÃ©', 'CR', 'CR-flag.gif'], ['Cuba', 'Havana', 'CU', 
'CU-flag.gif'], ['Cape Verde', 'Praia', 'CV', 'CV-flag.gif'], ['Cyprus', 'Nicosia', 'CY', 'CY-flag.gif'], ['Czech Republic', 'Prague', 'CZ', 'CZ-flag.gif'], ['Germany', 'Berlin', 'DE', 'DE-flag.gif'], ['Djibouti', 'Djibouti', 'DJ', 'DJ-flag.gif'], ['Denmark', 'Copenagen', 'DK', 'DK-flag.gif'], ['Dominica', 'Roseau', 'DM', 'DM-flag.gif'], ['Dominican Republic', 'Santo Domingo', 'DO', 'DO-flag.gif'], ['Algeria', 'Algiers', 'DZ', 'DZ-flag.gif'], ['Ecuador', 'Quito', 'EC', 
'EC-flag.gif'], ['Estonia', 'Tallinn', 'EE', 'EE-flag.gif'], ['Egypt', 'Cairo', 'EG', 'EG-flag.gif'], ['Eritrea', 'Asmara', 'ER', 'ER-flag.gif'], ['Spain', 'Madrid', 'ES', 'ES-flag.gif'], ['Ethiopia', 'Addis Ababa', 'ET', 'ET-flag.gif'], ['Finland', 'Helsinki', 'FI', 'FI-flag.gif'], ['Fiji', 'Suva', 'FJ', 'FJ-flag.gif'], ['Micronesia', 'Palikir', 'FM', 'FM-flag.gif'], ['France', 'Paris', 'FR', 'FR-flag.gif'], ['Gabon', 'Libreville', 'GA', 'GA-flag.gif'], ['United Kingdom', 'London', 'GB', 'GB-flag.gif'], ['Grenada', "St. George's", 'GD', 'GD-flag.gif'], ['Georgia', 'Tbilisi', 'GE', 'GE-flag.gif'], ['Ghana', 'Accra', 'GH', 'GH-flag.gif'], ['Gambia', 'Banjul', 'GM', 'GM-flag.gif'], ['Guinea', 'Conakry', 
'GN', 'GN-flag.gif'], ['Equatorial Guinea', 'Malabo', 'GQ', 'GQ-flag.gif'], ['Greece', 'Athens', 'GR', 'GR-flag.gif'], ['Guatemala', 'Guatemala City', 'GT', 'GT-flag.gif'], ['Guinea-Bissau', 'Bissau', 'GW', 'GW-flag.gif'], ['Guyana', 'Georgetown', 'GY', 'GY-flag.gif'], ['Honduras', 'Tegucigalpa', 'HN', 'HN-flag.gif'], ['Croatia', 'Zagreb', 'HR', 'HR-flag.gif'], ['Haiti', 'Port-au-Prince', 'HT', 'HT-flag.gif'], ['Hungary', 'Budapest', 'HU', 'HU-flag.gif'], ['Indonesia', 
'Jakarta', 'ID', 'ID-flag.gif'], ['Ireland', 'Dublin', 'IE', 'IE-flag.gif'], ['Israel', 'Jerusalem', 'IL', 'IL-flag.gif'], ['India', 'New Delhi', 'IN', 'IN-flag.gif'], ['Iraq', 'Baghdad', 'IQ', 'IQ-flag.gif'], ['Iran', 'Tehran', 'IR', 'IR-flag.gif'], ['Iceland', 'ReykjavÃ\xadk', 'IS', 'IS-flag.gif'], ['Italy', 'Rome', 'IT', 'IT-flag.gif'], ['Jamaica', 'Kingston', 'JM', 'JM-flag.gif'], ['Jordan', 'Amman', 'JO', 'JO-flag.gif'], ['Japan', 'Tokyo', 'JP', 'JP-flag.gif'], ['Kenya', 'Nairobi', 'KE', 'KE-flag.gif'], ['Kyrgyzstan', 'Bishkek', 'KG', 'KG-flag.gif'], ['Cambodia', 'Phnom Penh', 'KH', 'KH-flag.gif'], ['Kiribati', 'Tarawa', 'KI', 'KI-flag.gif'], ['Comoros', 'Moroni', 'KM', 'KM-flag.gif'], ['Saint Kitts and Nevis', 'Basseterre', 'KN', 'KN-flag.gif'], ['Korea, North', 'Pyongyang', 'KP', 'KP-flag.gif'], ['Korea, South', 'Seoul', 'KR', 'KR-flag.gif'], ['Kuwait', 'Kuwait City', 'KW', 'KW-flag.gif'], ['Kazakhstan', 'Astana', 'KZ', 'KZ-flag.gif'], ['Laos', 'Vientiane', 'LA', 'LA-flag.gif'], ['Lebanon', 'Beirut', 'LB', 'LB-flag.gif'], ['Saint Lucia', 'Castries', 'LC', 'LC-flag.gif'], ['Liechtenstein', 'Vaduz', 'LI', 'LI-flag.gif'], ['Sri Lanka', 'Sri Jayawardenapura Kotte', 'LK', 'LK-flag.gif'], ['Liberia', 'Monrovia', 'LR', 'LR-flag.gif'], ['Lesotho', 'Maseru', 'LS', 'LS-flag.gif'], ['Lithuania', 'Vilnius', 'LT', 'LT-flag.gif'], ['Luxembourg', 'Luxembourg', 'LU', 'LU-flag.gif'], ['Latvia', 'Riga', 'LV', 
'LV-flag.gif'], ['Libya', 'Tripoli', 'LY', 'LY-flag.gif'], ['Morocco', 'Rabat', 'MA', 'MA-flag.gif'], ['Monaco', 'Monaco', 'MC', 'MC-flag.gif'], ['Moldova', 'Chisinau', 'MD', 'MD-flag.gif'], ['Montenegro', 'Podgorica', 'ME', 'ME-flag.gif'], ['Madagascar', 'Antananarivo', 'MG', 'MG-flag.gif'], ['Marshall Islands', 'Majuro', 'MH', 'MH-flag.gif'], ['North Macedonia', 'Skopje', 'MK', 'MK-flag.gif'], ['Mali', 'Bamako', 'ML', 'ML-flag.gif'], ['Myanmar', 'Naypyidaw', 'MM', 'MM-flag.gif'], ['Mongolia', 'Ulaanbaatar', 'MN', 'MN-flag.gif'], ['Mauritania', 'Nouakchott', 'MR', 'MR-flag.gif'], ['Malta', 'Valletta', 'MT', 'MT-flag.gif'], ['Mauritius', 'Port Louis', 'MU', 'MU-flag.gif'], ['Maldives', 'MalÃ©', 'MV', 'MV-flag.gif'], ['Malawi', 'Lilongwe', 'MW', 'MW-flag.gif'], ['Mexico', 'Mexico City', 'MX', 'MX-flag.gif'], ['Malaysia', 'Kuala Lumpur', 'MY', 'MY-flag.gif'], ['Mozambique', 'Maputo', 'MZ', 'MZ-flag.gif'], ['Namibia', 'Windhoek', 'NA', 'NA-flag.gif'], ['Niger', 'Niamey', 'NE', 'NE-flag.gif'], ['Nigeria', 'Abuja', 'NG', 'NG-flag.gif'], ['Nicaragua', 'Managua', 'NI', 'NI-flag.gif'], ['Netherlands', 'Amsterdam', 'NL', 'NL-flag.gif'], ['Norway', 'Oslo', 'NO', 'NO-flag.gif'], ['Nepal', 'Kathmandu', 'NP', 'NP-flag.gif'], ['Nauru', 'Yaren', 'NR', 'NR-flag.gif'], ['New Zealand', 'Wellington', 'NZ', 'NZ-flag.gif'], ['Oman', 'Muscat', 'OM', 'OM-flag.gif'], ['Panama', 'Panama City', 'PA', 'PA-flag.gif'], ['Peru', 'Lima', 'PE', 'PE-flag.gif'], ['Papua New Guinea', 'Port Moresby', 'PG', 'PG-flag.gif'], ['Philippines', 'Manila', 'PH', 'PH-flag.gif'], ['Pakistan', 'Islamabad', 'PK', 'PK-flag.gif'], ['Poland', 'Warsaw', 'PL', 'PL-flag.gif'], ['Portugal', 'Lisbon', 'PT', 'PT-flag.gif'], ['Palau', 'Melekeok', 'PW', 'PW-flag.gif'], ['Paraguay', 'AsunciÃ³n', 'PY', 'PY-flag.gif'], ['Qatar', 'Doha', 'QA', 'QA-flag.gif'], ['Romania', 'Bucharest', 'RO', 'RO-flag.gif'], ['Serbia', 'Belgrade', 'RS', 'RS-flag.gif'], ['Russia', 'Moscow', 'RU', 'RU-flag.gif'], ['Rwanda', 'Kigali', 'RW', 'RW-flag.gif'], ['Saudi Arabia', 'Riyadh', 'SA', 'SA-flag.gif'], ['Solomon Islands', 'Honiara', 'SB', 'SB-flag.gif'], ['Seychelles', 'Victoria', 'SC', 'SC-flag.gif'], ['Sudan', 'Khartoum', 'SD', 'SD-flag.gif'], ['Sweden', 'Stockholm', 'SE', 'SE-flag.gif'], ['Singapore', 'Singapore', 'SG', 'SG-flag.gif'], ['Slovenia', 'Ljubljana', 'SI', 'SI-flag.gif'], ['Slovakia', 'Bratislava', 'SK', 'SK-flag.gif'], ['Sierra Leone', 'Freetown', 'SL', 'SL-flag.gif'], ['San Marino', 'San Marino', 'SM', 'SM-flag.gif'], ['Senegal', 'Dakar', 'SN', 'SN-flag.gif'], ['Somalia', 'Mogadishu', 'SO', 'SO-flag.gif'], ['Suriname', 'Paramaribo', 'SR', 'SR-flag.gif'], ['South Sudan', 'Juba', 'SS', 'SS-flag.gif'], ['SÃ£o TomÃ© and PrÃ\xadncipe', 'SÃ£o TomÃ©', 'ST', 'ST-flag.gif'], ['El Salvador', 'San Salvador', 'SV', 'SV-flag.gif'], ['Syria', 'Damascus', 'SY', 'SY-flag.gif'], ['Eswatini', 'Mbabane', 'SZ', 'SZ-flag.gif'], ['Chad', "N'Djamena", 'TD', 'TD-flag.gif'], ['Togo', 'LomÃ©', 'TG', 'TG-flag.gif'], ['Thailand', 'Bangkok', 'TH', 'TH-flag.gif'], ['Tajikistan', 'Dushanbe', 'TJ', 'TJ-flag.gif'], ['East Timor', 'Dili', 'TL', 'TL-flag.gif'], ['Turkmenistan', 'Ashgabat', 'TM', 'TM-flag.gif'], ['Tunisia', 'Tunis', 'TN', 'TN-flag.gif'], ['Tonga', 'Nukualofa', 'TO', 'TO-flag.gif'], ['Turkey', 'Ankara', 'TR', 'TR-flag.gif'], ['Trinidad and Tobago', 'Port of Spain', 'TT', 'TT-flag.gif'], ['Tuvalu', 'Funafuti', 'TV', 'TV-flag.gif'], ['Taiwan', 'Taipei', 'TW', 'TW-flag.gif'], ['Tanzania', 'Dodoma', 'TZ', 'TZ-flag.gif'], ['Ukraine', 'Kiev', 'UA', 'UA-flag.gif'], ['Uganda', 'Kampala', 'UG', 'UG-flag.gif'], ['United States', 'Washington D.C.', 'US', 'US-flag.gif'], ['Uruguay', 'Montevideo', 'UY', 'UY-flag.gif'], ['Uzbekistan', 'Tashkent', 'UZ', 'UZ-flag.gif'], ['Saint Vincent and the Grenadines', 'Kingstown', 'VC', 
'VC-flag.gif'], ['Venezuela', 'Caracas', 'VE', 'VE-flag.gif'], ['Vietnam', 'Hanoi', 'VN', 'VN-flag.gif'], ['Vanuatu', 'Port Vila', 'VU', 'VU-flag.gif'], ['Samoa', 'Apia', 'WS', 'WS-flag.gif'], ['Kosovo', 'Pristina', 'XK', 'XK-flag.gif'], ['Yemen', "Sana'a", 'YE', 'YE-flag.gif'], ['South Africa', 'Pretoria', 'ZA', 'ZA-flag.gif'], ['Zambia', 'Lusaka', 'ZM', 'ZM-flag.gif'], ['Zimbabwe', 'Harare', 'ZW', 'ZW-flag.gif']]

all_answers = []

chosen = random.choice(all_flags)
answer = chosen[0]

all_answers.append(answer)

while len(all_answers) < 4:
    wrong_choice_entry = random.choice(all_flags)
    wrong_choice = wrong_choice_entry[0]
    if wrong_choice not in all_answers: 
        all_answers.append(wrong_choice)
        
print("pre shuffle", all_answers)
                                                                            