from pymergecap.command.builder import build_mergecap_command
from pymergecap.command.runner import run_command
from pymergecap.config.config import mergecap_possible_locations
import os.path
import platform


class MergeCap():

    def __init__(self, mergecap_location=None):
        if mergecap_location is not None:
            if os.path.isfile(mergecap_location):
                self.mergecap_location = mergecap_location
            else:
                raise FileNotFoundError

        self.mergecap_location = self.__find_mergecap_location()

    def merge(self, input_files, output_file, ignore_frame_timestamps=False, output_file_format=None, snapshot_length=None, idb_merge_mode=None):
        command = build_mergecap_command(self.mergecap_location, input_files, output_file,
                                         False, ignore_frame_timestamps, output_file_format, snapshot_length, idb_merge_mode)
        run_command(command)

    def __find_mergecap_location(self):
        system = platform.system()
        possible_locations = mergecap_possible_locations[system]
        for possible_location in possible_locations:
            if os.path.isfile(possible_location):
                return possible_location
        raise FileNotFoundError

    def get_version(self):
        command = build_mergecap_command(get_version=True)
        return run_command(command)
