class ModelRunner:
  def __init__(self, model_name):
    self.model_name = model_name
    self.queue = []

    self.queue_lock = None

    self.model = get_pretrained_model(self.model_name,
                  map_location=device)
    self.needs_processing = None
    self.needs_processing_timer = None