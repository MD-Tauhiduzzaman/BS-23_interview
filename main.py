from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
driver= webdriver.Chrome(r"resource/chromedriver.exe")
url = "http://automationpractice.com/index.php"
driver.get(url)

driver.maximize_window()
time.sleep(2)
driver.find_element_by_partial_link_text("Sign").click()

driver.find_element_by_css_selector("#email").send_keys("tauhiduzzaman.btrac@gmail.com")
driver.find_element_by_css_selector("#passwd").send_keys("ABCDE")

driver.find_element_by_css_selector("body.authentication.hide-left-column.hide-right-column.lang_en:nth-child(2) div.columns-container div.container div.row:nth-child(3) div.center_column.col-xs-12.col-sm-12 div.row div.col-xs-12.col-sm-6:nth-child(2) form.box div.form_content.clearfix p.submit:nth-child(4) button.button.btn.btn-default.button-medium > span:nth-child(1)").click()

driver.find_element_by_xpath("//body[1]/div[1]/div[1]/header[1]/div[3]/div[1]/div[1]/div[6]/ul[1]/li[2]/a[1]").click()
driver.find_element_by_css_selector("body.category.category-8.category-dresses.hide-right-column.lang_en:nth-child(2) div.columns-container div.container div.row:nth-child(3) div.center_column.col-xs-12.col-sm-9 div.content_sortPagiBar.clearfix:nth-child(4) div.sortPagiBar.clearfix ul.display.hidden-xs li:nth-child(3) a:nth-child(1) > i.icon-th-list").click()


#driver.find_element_by_xpath("//body[1]/div[1]/div[2]/div[1]/div[3]/div[2]/ul[1]/li[1]/div[1]/div[1]/div[3]/div[1]/div[2]/a[1]/span[1]").click()
#driver.find_element_by_xpath("//body[1]/div[1]/div[1]/header[1]/div[3]/div[1]/div[1]/div[4]/div[1]/div[2]/div[4]/a[1]/span[1]").click()


driver.find_element_by_css_selector("body.category.category-8.category-dresses.hide-right-column.lang_en:nth-child(2) div.columns-container div.container div.row:nth-child(3) div.center_column.col-xs-12.col-sm-9 ul.product_list.row.list:nth-child(5) li.ajax_block_product.first-in-line.first-item-of-tablet-line.first-item-of-mobile-line.col-xs-12:nth-child(1) div.product-container div.row div.right-block.col-xs-4.col-xs-12.col-md-4 div.right-block-content.row div.button-container.col-xs-7.col-md-12 a.button.lnk_view.btn.btn-default:nth-child(2) > span:nth-child(1)").click()
driver.find_element_by_css_selector("body.product.product-3.product-printed-dress.category-8.category-dresses.hide-left-column.hide-right-column.lang_en:nth-child(2) div.columns-container div.container div.row:nth-child(3) div.center_column.col-xs-12.col-sm-12 div.primary_block.row:nth-child(1) div.pb-right-column.col-xs-12.col-sm-4.col-md-3 div.box-info-product div.box-cart-bottom div:nth-child(1) p.buttons_bottom_block.no-print button.exclusive > span:nth-child(1)").click()
time.sleep(3)
driver.find_element_by_css_selector("body.product.product-3.product-printed-dress.category-8.category-dresses.hide-left-column.hide-right-column.lang_en:nth-child(2) div.header-container div.container div.row div.clearfix div.layer_cart_cart.col-xs-12.col-md-6 div.button-container:nth-child(5) a.btn.btn-default.button.button-medium > span:nth-child(1)").click()
driver.find_element_by_css_selector("body.order.hide-left-column.hide-right-column.lang_en:nth-child(2) div.columns-container div.container div.row:nth-child(3) div.center_column.col-xs-12.col-sm-12 p.cart_navigation.clearfix:nth-child(8) a.button.btn.btn-default.standard-checkout.button-medium > span:nth-child(1)").click()
driver.find_element_by_css_selector("body.order.hide-left-column.hide-right-column.lang_en:nth-child(2) div.columns-container div.container div.row:nth-child(3) div.center_column.col-xs-12.col-sm-12 form:nth-child(3) p.cart_navigation.clearfix button.button.btn.btn-default.button-medium:nth-child(4) > span:nth-child(1)").click()
driver.find_element_by_css_selector("#cgv").click()
driver.find_element_by_css_selector("body.order.hide-left-column.hide-right-column.lang_en:nth-child(2) div.columns-container div.container div.row:nth-child(3) div.center_column.col-xs-12.col-sm-12 div:nth-child(1) form:nth-child(3) p.cart_navigation.clearfix button.button.btn.btn-default.standard-checkout.button-medium:nth-child(4) > span:nth-child(1)").click()
driver.find_element_by_css_selector("body.order.hide-left-column.hide-right-column.lang_en:nth-child(2) div.columns-container div.container div.row:nth-child(3) div.center_column.col-xs-12.col-sm-12 div.paiement_block div:nth-child(3) div.row:nth-child(1) div.col-xs-12.col-md-6 p.payment_module > a.bankwire").click()
driver.find_element_by_css_selector("body.module-bankwire-payment.hide-left-column.hide-right-column.lang_en:nth-child(2) div.columns-container div.container div.row:nth-child(3) div.center_column.col-xs-12.col-sm-12 form:nth-child(3) p.cart_navigation.clearfix button.button.btn.btn-default.button-medium > span:nth-child(1)").click()

#order_2

driver.find_element_by_xpath("//body[1]/div[1]/div[1]/header[1]/div[3]/div[1]/div[1]/div[6]/ul[1]/li[2]/a[1]").click()

driver.find_element_by_css_selector("body.category.category-8.category-dresses.hide-right-column.lang_en:nth-child(2) div.columns-container div.container div.row:nth-child(3) div.center_column.col-xs-12.col-sm-9 ul.product_list.row.list:nth-child(5) li.ajax_block_product.last-item-of-tablet-line.col-xs-12:nth-child(2) div.product-container div.row div.right-block.col-xs-4.col-xs-12.col-md-4 div.right-block-content.row div.button-container.col-xs-7.col-md-12 a.button.lnk_view.btn.btn-default:nth-child(2) > span:nth-child(1)").click()
driver.find_element_by_css_selector("body.product.product-4.product-printed-dress.category-8.category-dresses.hide-left-column.hide-right-column.lang_en:nth-child(2) div.columns-container div.container div.row:nth-child(3) div.center_column.col-xs-12.col-sm-12 div.primary_block.row:nth-child(1) div.pb-right-column.col-xs-12.col-sm-4.col-md-3 div.box-info-product div.box-cart-bottom div:nth-child(1) p.buttons_bottom_block.no-print button.exclusive > span:nth-child(1)").click()
time.sleep(3)
driver.find_element_by_css_selector("body.product.product-4.product-printed-dress.category-8.category-dresses.hide-left-column.hide-right-column.lang_en:nth-child(2) div.header-container div.container div.row div.clearfix div.layer_cart_cart.col-xs-12.col-md-6 div.button-container:nth-child(5) a.btn.btn-default.button.button-medium > span:nth-child(1)").click()
driver.find_element_by_css_selector("body.order.hide-left-column.hide-right-column.lang_en:nth-child(2) div.columns-container div.container div.row:nth-child(3) div.center_column.col-xs-12.col-sm-12 p.cart_navigation.clearfix:nth-child(8) a.button.btn.btn-default.standard-checkout.button-medium > span:nth-child(1)").click()
driver.find_element_by_css_selector("body.order.hide-left-column.hide-right-column.lang_en:nth-child(2) div.columns-container div.container div.row:nth-child(3) div.center_column.col-xs-12.col-sm-12 form:nth-child(3) p.cart_navigation.clearfix button.button.btn.btn-default.button-medium:nth-child(4) > span:nth-child(1)").click()
driver.find_element_by_css_selector("#cgv").click()
driver.find_element_by_css_selector("body.order.hide-left-column.hide-right-column.lang_en:nth-child(2) div.columns-container div.container div.row:nth-child(3) div.center_column.col-xs-12.col-sm-12 div:nth-child(1) form:nth-child(3) p.cart_navigation.clearfix button.button.btn.btn-default.standard-checkout.button-medium:nth-child(4) > span:nth-child(1)").click()
driver.find_element_by_css_selector("body.order.hide-left-column.hide-right-column.lang_en:nth-child(2) div.columns-container div.container div.row:nth-child(3) div.center_column.col-xs-12.col-sm-12 div.paiement_block div:nth-child(3) div.row:nth-child(1) div.col-xs-12.col-md-6 p.payment_module > a.bankwire").click()
driver.find_element_by_css_selector("body.module-bankwire-payment.hide-left-column.hide-right-column.lang_en:nth-child(2) div.columns-container div.container div.row:nth-child(3) div.center_column.col-xs-12.col-sm-12 form:nth-child(3) p.cart_navigation.clearfix button.button.btn.btn-default.button-medium > span:nth-child(1)").click()


