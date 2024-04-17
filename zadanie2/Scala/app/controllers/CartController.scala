package controllers

import javax.inject._
import play.api.mvc._
import play.api.libs.json._
import models.{Cart, CartItem}

@Singleton
class CartController @Inject()(cc: ControllerComponents) extends AbstractController(cc) {
    var carts: List[Cart] = List()

    def getCart(id: Long) = Action {
        carts.find(_.id == id).map(cart => Ok(Json.toJson(cart))).getOrElse(NotFound)
    }

    def updateCart(id: Long) = Action(parse.json) { request =>
        request.body.validate[Cart].map { updatedCart =>
            carts = carts.map {
                case c if c.id == id => updatedCart
                case c => c
            }
            Ok(Json.toJson(updatedCart))
        }.recoverTotal {
            _ => BadRequest("Invalid JSON")
        }
    }

    def addCart = Action(parse.json) { request =>
        request.body.validate[Cart].map { cart =>
            carts = carts :+ cart
            Created(Json.toJson(cart))
        }.recoverTotal {
            _ => BadRequest("Invalid JSON")
        }
    }

    def deleteCart(id: Long) = Action {
        carts = carts.filterNot(_.id == id)
        NoContent
    }
}