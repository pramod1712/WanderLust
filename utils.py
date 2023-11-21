import inspect
import textwrap

import streamlit as st
from st_clickable_images import clickable_images
from serpapi import GoogleSearch


def show_code(demo):
    """Showing the code of the demo."""
    show_code = st.sidebar.checkbox("Show code", True)
    if show_code:
        # Showing the code of the demo.
        st.markdown("## Code")
        sourcelines, _ = inspect.getsourcelines(demo)
        st.code(textwrap.dedent("".join(sourcelines[1:])))

countries_info = {'Afghanistan': 'AFG', 'Albania': 'ALB', 'Algeria': 'DZA', 'American Samoa': 'ASM', 'Andorra': 'AND', 'Angola': 'AGO', 'Anguila': 'AIA', 'Antigua and Barbuda': 'ATG', 'Argentina': 'ARG', 'Armenia': 'ARM', 'Aruba': 'ABW', 'Australia': 'AUS', 'Austria': 'AUT', 'Azerbaijan': 'AZE', 'Bahamas, The': 'BHS', 'Bahrain': 'BHR', 'Bangladesh': 'BGD', 'Barbados': 'BRB', 'Belarus': 'BLR', 'Belgium': 'BEL', 'Belgium-Luxembourg': 'BLX', 'Belize': 'BLZ', 'Benin': 'BEN', 'Bermuda': 'BMU', 'Bhutan': 'BTN', 'Bolivia': 'BOL', 'Bosnia and Herzegovina': 'BIH', 'Botswana': 'BWA', 'Br. Antr. Terr': 'BAT', 'Brazil': 'BRA', 'British Indian Ocean Ter.': 'IOT', 'British Virgin Islands': 'VGB', 'Brunei': 'BRN', 'Bulgaria': 'BGR', 'Burkina Faso': 'BFA', 'Burundi': 'BDI', 'Cambodia': 'KHM', 'Cameroon': 'CMR', 'Canada': 'CAN', 'Cape Verde': 'CPV', 'Cayman Islands': 'CYM', 'Central African Republic': 'CAF', 'Chad': 'TCD', 'Chile': 'CHL', 'China': 'CHN', 'Christmas Island': 'CXR', 'Cocos (Keeling) Islands': 'CCK', 'Colombia': 'COL', 'Comoros': 'COM', 'Congo, Dem. Rep.': 'ZAR', 'Congo, Rep.': 'COG', 'Cook Islands': 'COK', 'Costa Rica': 'CRI', "Cote d'Ivoire": 'CIV', 'Croatia': 'HRV', 'Cuba': 'CUB', 'Cyprus': 'CYP', 'Czech Republic': 'CZE', 'Czechoslovakia': 'CSK', 'Denmark': 'DNK', 'Djibouti': 'DJI', 'Dominica': 'DMA', 'Dominican Republic': 'DOM', 'East Timor': 'TMP', 'Ecuador': 'ECU', 'Egypt, Arab Rep.': 'EGY', 'El Salvador': 'SLV', 'Equatorial Guinea': 'GNQ', 'Eritrea': 'ERI', 'Estonia': 'EST', 'Ethiopia (excludes Eritrea)': 'ETH', 'Ethiopia (includes Eritrea)': 'ETF', 'European Union': 'EUN', 'Faeroe Islands': 'FRO', 'Falkland Island': 'FLK', 'Fiji': 'FJI', 'Finland': 'FIN', 'Fm Panama Cz': 'PCZ', 'Fm Rhod Nyas': 'ZW1', 'Fm Tanganyik': 'TAN', 'Fm Vietnam Dr': 'VDR', 'Fm Vietnam Rp': 'SVR', 'Fm Zanz-Pemb': 'ZPM', 'Fr. So. Ant. Tr': 'ATF', 'France': 'FRA', 'Free Zones': 'FRE', 'French Guiana': 'GUF', 'French Polynesia': 'PYF', 'Gabon': 'GAB', 'Gambia, The': 'GMB', 'Gaza Strip': 'GAZ', 'Georgia': 'GEO', 'German Democratic Republic': 'DDR', 'Germany': 'DEU', 'Ghana': 'GHA', 'Gibraltar': 'GIB', 'Greece': 'GRC', 'Greenland': 'GRL', 'Grenada': 'GRD', 'Guadeloupe': 'GLP', 'Guam': 'GUM', 'Guatemala': 'GTM', 'Guinea': 'GIN', 'Guinea-Bissau': 'GNB', 'Guyana': 'GUY', 'Haiti': 'HTI', 'Holy See': 'VAT', 'Honduras': 'HND', 'Hong Kong, China': 'HKG', 'Hungary': 'HUN', 'Iceland': 'ISL', 'India': 'IND', 'Indonesia': 'IDN', 'Iran, Islamic Rep.': 'IRN', 'Iraq': 'IRQ', 'Ireland': 'IRL', 'Israel': 'ISR', 'Italy': 'ITA', 'Jamaica': 'JAM', 'Japan': 'JPN', 'Jhonston Island': 'JTN', 'Jordan': 'JOR', 'Kazakhstan': 'KAZ', 'Kenya': 'KEN', 'Kiribati': 'KIR', 'Korea, Dem. Rep.': 'PRK', 'Korea, Rep.': 'KOR', 'Kuwait': 'KWT', 'Kyrgyz Republic': 'KGZ', 'Lao PDR': 'LAO', 'Latvia': 'LVA', 'Lebanon': 'LBN', 'Lesotho': 'LSO', 'Liberia': 'LBR', 'Libya': 'LBY', 'Liechtenstein': 'LIE', 'Lithuania': 'LTU', 'Luxembourg': 'LUX', 'Macao': 'MAC', 'Macedonia, FYR': 'MKD', 'Madagascar': 'MDG', 'Malawi': 'MWI', 'Malaysia': 'MYS', 'Maldives': 'MDV', 'Mali': 'MLI', 'Malta': 'MLT', 'Marshall Islands': 'MHL', 'Martinique': 'MTQ', 'Mauritania': 'MRT', 'Mauritius': 'MUS', 'Mexico': 'MEX', 'Micronesia, Fed. Sts.': 'FSM', 'Midway Islands': 'MID', 'Moldova': 'MDA', 'Monaco': 'MCO', 'Mongolia': 'MNG', 'Montserrat': 'MSR', 'Morocco': 'MAR', 'Mozambique': 'MOZ', 'Myanmar': 'MMR', 'Namibia': 'NAM', 'Nauru': 'NRU', 'Nepal': 'NPL', 'Netherlands': 'NLD', 'Netherlands Antilles': 'ANT', 'Neutral Zone': 'NZE', 'New Caledonia': 'NCL', 'New Zealand': 'NZL', 'Nicaragua': 'NIC', 'Niger': 'NER', 'Nigeria': 'NGA', 'Niue': 'NIU', 'Norfolk Island': 'NFK', 'Northern Mariana Islands': 'MNP', 'Norway': 'NOR', 'Oman': 'OMN', 'Pacific Islands': 'PCE', 'Pakistan': 'PAK', 'Palau': 'PLW', 'Panama': 'PAN', 'Papua New Guinea': 'PNG', 'Paraguay': 'PRY', 'Pen Malaysia': 'PMY', 'Peru': 'PER', 'Philippines': 'PHL', 'Pitcairn': 'PCN', 'Poland': 'POL', 'Portugal': 'PRT', 'Puerto Rico': 'PRI', 'Qatar': 'QAT', 'Reunion': 'REU', 'Romania': 'ROM', 'Russian Federation': 'RUS', 'Rwanda': 'RWA', 'Ryukyu Is': 'RYU', 'Sabah': 'SBH', 'Saint Helena': 'SHN', 'Saint Kitts-Nevis-Anguilla-Aru': 'KN1', 'Saint Pierre and Miquelon': 'SPM', 'Samoa': 'WSM', 'San Marino': 'SMR', 'Sao Tome and Principe': 'STP', 'Sarawak': 'SWK', 'Saudi Arabia': 'SAU', 'Senegal': 'SEN', 'Seychelles': 'SYC', 'Sierra Leone': 'SLE', 'SIKKIM': 'SIK', 'Singapore': 'SGP', 'Slovak Republic': 'SVK', 'Slovenia': 'SVN', 'Solomon Islands': 'SLB', 'Somalia': 'SOM', 'South Africa': 'ZAF', 'Soviet Union': 'SVU', 'Spain': 'ESP', 'Special Categories': 'SPE', 'Sri Lanka': 'LKA', 'St. Kitts and Nevis': 'KNA', 'St. Lucia': 'LCA', 'St. Vincent and the Grenadines': 'VCT', 'Sudan': 'SDN', 'Suriname': 'SUR', 'Svalbard and Jan Mayen Is': 'SJM', 'Swaziland': 'SWZ', 'Sweden': 'SWE', 'Switzerland': 'CHE', 'Syrian Arab Republic': 'SYR', 'Taiwan': 'TWN', 'Tajikistan': 'TJK', 'Tanzania': 'TZA', 'Thailand': 'THA', 'Togo': 'TGO', 'Tokelau': 'TKL', 'Tonga': 'TON', 'Trinidad and Tobago': 'TTO', 'Tunisia': 'TUN', 'Turkey': 'TUR', 'Turkmenistan': 'TKM', 'Turks and Caicos Isl.': 'TCA', 'Tuvalu': 'TUV', 'Uganda': 'UGA', 'Ukraine': 'UKR', 'United Arab Emirates': 'ARE', 'United Kingdom': 'GBR', 'United States': 'USA', 'Unspecified': 'UNS', 'Uruguay': 'URY', 'Us Msc.Pac.I': 'USP', 'Uzbekistan': 'UZB', 'Vanuatu': 'VUT', 'Venezuela': 'VEN', 'Vietnam': 'VNM', 'Virgin Islands (U.S.)': 'VIR', 'Wake Island': 'WAK', 'Wallis and Futura Isl.': 'WLF', 'Western Sahara': 'ESH', 'World': 'WLD', 'Yemen Democratic': 'YDR', 'Yemen, Rep.': 'YEM', 'Yugoslavia': 'SER', 'Yugoslavia, FR (Serbia/Montene': 'YUG', 'Zambia': 'ZMB', 'Zimbabwe': 'ZWE'}

def get_country_code(country_name):
    # Convert the country name to title case for consistent matching
    country_name = country_name.title()

    # Check if the country name exists in the dictionary
    if country_name in countries_info.keys():
        return countries_info[country_name]
    else:
        return "Country code not found"

def serpapi_get_google_images(api_key):
    image_results = set()  # Use a set to store unique URLs
    queries = ["Taj Mahal", "Mount Fuji"]
    num_images_per_query = 5  # Fetch more images per query

    params = {
        "engine": "google",
        "q": ",".join(queries),  # Combine all queries into a single search
        "tbm": "isch",
        "num": str(num_images_per_query),
        "ijn": 0,
        "safe": "active",
        "api_key": api_key
    }

    search = GoogleSearch(params)
    images_are_present = True

    while images_are_present:
        results = search.get_dict()

        if "error" not in results:
            for image in results["images_results"]:
                image_results.add(image["original"])  # Add unique URLs to the set

            params["ijn"] += 1
        else:
            images_are_present = False
            print(results["error"])

    return image_results

serpapi_key = st.secrets["serpapi_key"]
image_urls = serpapi_get_google_images(serpapi_key)

for index, url in enumerate(image_urls, start=1):
    st.write(f"Image {index} URL: {url}")

st.write(f"Total Unique Images: {len(image_urls)}")

def get_images():
    clicked = clickable_images(
                [
                    "https://images.unsplash.com/photo-1565130838609-c3a86655db61?w=700",
                    "https://images.unsplash.com/photo-1565372195458-9de0b320ef04?w=700",
                    "https://images.unsplash.com/photo-1582550945154-66ea8fff25e1?w=700",
                    "https://images.unsplash.com/photo-1591797442444-039f23ddcc14?w=700",
                    "https://unsplash.com/photos/a-bunch-of-white-daisies-are-in-motion-OXl_Bm4Y-yU",
                ],
                titles=[f"Image #{str(i)}" for i in range(5)],
                div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
                img_style={"margin": "5px", "height": "200px"},
)

    st.markdown(f"Image #{clicked} clicked" if clicked > -1 else "No image clicked")

