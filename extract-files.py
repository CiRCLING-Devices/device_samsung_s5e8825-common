#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)
from extract_utils.fixups_lib import (
    lib_fixups_user_type,
)

module = ExtractUtilsModule(
    's5e8825-common',
    'samsung',
)

def lib_fixup_device_dep(lib: str, partition: str, *args, **kwargs):
    return f'//device/samsung/s5e8825-common/shims/stub:{lib}'


lib_fixups: lib_fixups_user_type = {
    'libexynoscamera3': lib_fixup_device_dep,
}  # fmt: skip

blob_fixups: blob_fixups_user_type = {
   (
        'vendor/lib/libaudioparamupdate.so',
        'vendor/lib/libaboxpcmdump.so',
        'vendor/lib/libaudioproxy2.so',
        'vendor/lib64/libaudioparamupdate.so',
        'vendor/lib64/libaboxpcmdump.so',
        'vendor/lib64/libaudioproxy2.so',
    ): blob_fixup()
        .add_needed('libaudioroute.s5e8825.so')
        .add_needed('libtinyalsa.s5e8825.so'),
    (
        'vendor/lib/hw/audio.primary.s5e8825.so',
        'vendor/lib64/hw/audio.primary.s5e8825.so'
    ): blob_fixup()
        .replace_needed('libaudioroute.so', 'libaudioroute.s5e8825.so')
        .replace_needed('libtinyalsa.so', 'libtinyalsa.s5e8825.so'),
}  # fmt: skip

module = ExtractUtilsModule(
    's5e8825-common',
    'samsung',
    blob_fixups=blob_fixups,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
