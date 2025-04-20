from browser_use.controller.service import Controller

from models.checkout_result import CheckoutResult


def setup_shopping_controller():
    controller = Controller(output_model=CheckoutResult)
    return controller
