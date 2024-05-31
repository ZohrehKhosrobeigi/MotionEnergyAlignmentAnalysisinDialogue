class PairingFiles():
    def pairingFiles(self,list_files1,list_files2,matchpoints):
        self.dict_pairedfiles = {}
        for number in matchpoints:
            z=[file for file in list_files1 if number in file]
            matching_files = [file for file in list_files1 if number in file] + [file for file in list_files2 if number in file]
            self.dict_pairedfiles[number] = matching_files
        return self.dict_pairedfiles
