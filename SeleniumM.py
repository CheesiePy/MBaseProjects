import bs4
import RequestModel

rh = RequestModel.RequestHandler('https://www.amazon.com/Dungeons-Dragons-Monster-Rulebook-Roleplaying/dp/0786965614/ref=pd_sbs_sccl_1_2/141-9350456-6057300?pd_rd_w=r2ewl&content-id=amzn1.sym.3676f086-9496-4fd7-8490-77cf7f43f846&pf_rd_p=3676f086-9496-4fd7-8490-77cf7f43f846&pf_rd_r=9JQV5QF5FWNXS4E1D95R&pd_rd_wg=mCVgR&pd_rd_r=3c5c0513-7050-4ef4-b061-13d319cb901c&pd_rd_i=0786965614&psc=1')
soup = bs4.BeautifulSoup(rh.get_request(), 'html.parser')
print(soup.prettify())
# elements = soup.select('#corePriceDisplay_desktop_feature_div > div.a-section.a-spacing-none.aok-align-center > span.a-price.aok-align-center.reinventPricePriceToPayMargin.priceToPay > span:nth-child(2) > span.a-price-whole')
# print(elements)