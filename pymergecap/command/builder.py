
def build_mergecap_command(mergecap_location, input_files, output_file, get_version=False, ignore_frame_timestamps=False, output_file_format=None, snapshot_length=None, idb_merge_mode=None):
    if get_version:
        return [mergecap_location, '-V']

    command = [mergecap_location, '-w', output_file]
    if ignore_frame_timestamps:
        command.append('-a')
    if output_file_format is not None:
        command.extend(['-F', output_file_format])
    if snapshot_length is not None:
        command.extend(['-s', snapshot_length])
    if idb_merge_mode is not None:
        command.extend(['-I', idb_merge_mode])
    command.extend(input_files)
    return command
