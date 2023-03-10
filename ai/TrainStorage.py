import os.path

from ai.consts import STORAGE_NAME

class TrainStorage:
  def __init__(self) -> None:
    self.file = open(STORAGE_NAME, 'w')
    text = 'generation,genome,fitness,hits,scored\n'
    self._write(text)

  def add_genome_info(self, generation, genome_id, genome_fitness, hits, scored):
    text = f'{generation},{genome_id},{genome_fitness},{hits},{scored}\n'
    self._write(text)
    
  def close(self):
    self.file.close()

  def _write(self, text):
    self.file.write(text)
    self.file.flush()