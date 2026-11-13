from harmony import DataPacket
import pyarrow.parquet as pq

from harmony import Step


class DataLoader(Step):
    def run(self, data_path) -> DataPacket:
        table = pq.read_table(data_path)
        data_dict = table.to_pylist()[0]
        return DataPacket(**data_dict)
