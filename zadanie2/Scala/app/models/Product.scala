package models

import play.api.data._
import play.api.data.Forms._

case class Product(id: Long, name: String, categoryId: Long, price: Double, description: Option[String])

object Product {
  val productForm: Form[Product] = Form(
    mapping(
      "id" -> longNumber,
      "name" -> nonEmptyText,
      "categoryId" -> longNumber,
      "price" -> bigDecimal,
      "description" -> optional(text)
    )(Product.apply)(Product.unapply)
  )
}