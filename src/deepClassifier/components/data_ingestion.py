
from deepClassifier import logger
from urllib import request
from zipfile import ZipFile
import os
from deepClassifier.entity.config_entity import DataIngestionConfig
from tqdm import tqdm
class DataIngestion:

    def __init__(self,config:DataIngestionConfig):
        self.config = config
    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            try:
                logger.info(f"Started downloading from : {self.config.source_URL}")
                filename , headers = request.urlretrieve(url=self.config.source_URL,
                filename=self.config.local_data_file)
                logger.info(f"file: {filename} downloaded with header : {headers}")
            except Exception as e:
                logger.exception(e)
        else:
            logger.info(f"file: {self.config.local_data_file} already downloaded")
                
            
    def _get_updated_list_of_files(self,list_of_files):
        return [f for f in list_of_files if f.endswith(".jpg") and ("Cat" in f or "Dog" in f)]

    def _preprocess(self,zf:ZipFile,f:str,working_dir:str):
        target_file_path = os.path.join(working_dir,f)
        if not os.path.exists(target_file_path):
            zf.extract(f,working_dir)
            
        if os.path.getsize(target_file_path) == 0:
            logger.info(f"removing file : {target_file_path} with size with 0 Kb")
            os.remove(target_file_path)

    def unzip_and_clean(self):
        try:
            logger.info(f"Unzipping file: {self.config.local_data_file}")
            with ZipFile(file=self.config.local_data_file,mode="r") as zf :
                list_of_files = zf.namelist()
                updated_list_of_files = self._get_updated_list_of_files(list_of_files=list_of_files)
                
                for f in tqdm(updated_list_of_files):
                    self._preprocess(zf,f,self.config.unzip_dir)

        except Exception as e:
            logger.exception(e)
                