from ai.consts import STORAGE_FILENAME

class TrainStorage:
  def __init__(self, generation=None) -> None:
    creation_option = 'w' if generation == None else 'a'
    self.file = open(STORAGE_FILENAME, creation_option)

    if generation == None:
      text = 'generation,genome,fitness,hits,scored\n'
      self._write(text)
      self.file.flush()

  def add_genome_info(self, generation, genome_id, genome_fitness, hits, scored):
    text = f'{generation},{genome_id},{genome_fitness},{hits},{scored}\n'
    self._write(text)
    
  def end_generation(self):
    self.file.flush()
  
  def close(self):
    self.file.close()

  def _write(self, text):
    self.file.write(text)