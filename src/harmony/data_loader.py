from harmony import DataPacket
import pyarrow.parquet as pq


def data_loader(data_path):
    table = pq.read_table(data_path)
    data_dict = table.to_pylist()[0]
    return DataPacket(**data_dict)
