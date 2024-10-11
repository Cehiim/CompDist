class OrderService:
    def __init__(self):
        self.payment_service = PaymentService()
        self.inventory_service = InventoryService()
        self.notification_service = NotificationService()

    def process_order(self, order):
        # Orquestração do fluxo
        payment_success = self.payment_service.process_payment(order)
        if not payment_success:
            print("Pagamento falhou!")
            return "Pedido não processado."

        inventory_success = self.inventory_service.update_inventory(order)
        if not inventory_success:
            print("Atualização de inventário falhou!")
            return "Pedido não processado."

        self.notification_service.send_confirmation(order)
        print("Pedido processado com sucesso!")
        return "Pedido processado com sucesso."

class PaymentService:
    def process_payment(self, order):
        # Lógica de pagamento
        print("Processando pagamento...")
        return True

class InventoryService:
    def update_inventory(self, order):
        # Lógica de inventário
        print("Atualizando inventário...")
        return True

class NotificationService:
    def send_confirmation(self, order):
        # Lógica de notificação
        print("Enviando confirmação de pedido...")

# Exemplo de uso
order_service = OrderService()
order = {"id": 123, "itens": ["item1", "item2"]}
order_service.process_order(order)
