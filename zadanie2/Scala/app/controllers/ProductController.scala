// ProductController.scala
package controllers

import javax.inject._
import play.api.mvc._
import play.api.libs.json._
import models.Product

@Singleton
class ProductController @Inject()(cc: ControllerComponents) extends AbstractController(cc) {
    var products: List[Product] = List(
        Product(1, "Laptop", 1, 1500.00),
        Product(2, "Smartphone", 2, 700.00)
    )

    def getAllProducts = Action {
        Ok(Json.toJson(products))
    }

    def getProduct(id: Long) = Action {
        products.find(_.id == id).map(product => Ok(Json.toJson(product))).getOrElse(NotFound)
    }

    def addProduct = Action(parse.json) { request =>
        request.body.validate[Product].map { product =>
            products = products :+ product
            Created(Json.toJson(product))
        }.recoverTotal {
            _ => BadRequest("Invalid JSON")
        }
    }

    def updateProduct(id: Long) = Action(parse.json) { request =>
        request.body.validate[Product].map { product =>
            products = products.map {
                case p if p.id == id => product
                case p => p
            }
            Ok(Json.toJson(product))
        }.recoverTotal {
            _ => BadRequest("Invalid JSON")
        }
    }

    def deleteProduct(id: Long) = Action {
        products = products.filterNot(_.id == id)
        NoContent
    }
}