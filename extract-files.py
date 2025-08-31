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
    'vendor/lib64/vendor.samsung.hardware.keymint-V1-ndk_platform.so': blob_fixup()
        .replace_needed('android.hardware.security.keymint-V1-ndk_platform.so',
            'android.hardware.security.keymint-V4-ndk.so')
        .replace_needed('android.hardware.security.keymint-V1-ndk_platform',
            'android.hardware.security.keymint-V4-ndk')
        .replace_needed('android.hardware.security.keymint-V1-ndk',
            'android.hardware.security.keymint-V4-ndk')
        .replace_needed('android.hardware.security.secureclock-V1-ndk_platform.so',
            'android.hardware.security.secureclock-V1-ndk.so')
        .replace_needed('android.hardware.security.sharedsecret-V1-ndk_platform.so',
             'android.hardware.security.sharedsecret-V1-ndk.so')
        .add_needed('android.hardware.security.rkp-V3-ndk.so')
        .replace_needed('libcrypto.so', 'libcrypto-tm.so')
        .replace_needed('libssl.so', 'libssl-tm.so')
        .add_needed('libshim_crypto.so'),
    'vendor/etc/init/android.hardware.security.keymint-service.samsung.rc': blob_fixup()
        .regex_replace('android\\.hardware\\.security\\.keymint-service\n',
            'android.hardware.security.keymint-service.samsung\n'),
    'vendor/lib64/libsensorlistener.so': blob_fixup()
        .add_needed('libshim_sensorndkbridge.so'),
    (
        'vendor/lib/sensors.grip.so',
        'vendor/lib/sensors.inputvirtual.so',
        'vendor/lib/sensors.sensorhub.so',
        'vendor/lib64/sensors.grip.so',
        'vendor/lib64/sensors.inputvirtual.so',
        'vendor/lib64/sensors.sensorhub.so',
    ): blob_fixup()
        .remove_needed('libhidltransport.so')
        .add_needed('libutils-v32.so')
        .binary_regex_replace(b'_ZN7android6Thread3runEPKcim', b'_ZN7utils326Thread3runEPKcim'),
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
    'vendor/lib64/libsec-ril.so': blob_fixup()
        .sig_replace('80 0E 40 F9 E1 03 16 AA 82 0C 80 52 E3 03 15 AA',
            '80 0E 40 F9 E1 03 16 AA 82 0C 80 52 03 00 80 D2'),
}  # fmt: skip

module = ExtractUtilsModule(
    's5e8825-common',
    'samsung',
    blob_fixups=blob_fixups,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
