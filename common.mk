#
# Copyright (C) The LineageOS Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Inherit the proprietary files
$(call inherit-product, vendor/samsung/s5e8825-common/s5e8825-common-vendor.mk)

# Graphics
PRODUCT_AAPT_CONFIG := normal
PRODUCT_AAPT_PREF_CONFIG := 450dpi
PRODUCT_AAPT_PREBUILT_DPI := xxxhdpi xxhdpi xhdpi hdpi

# Init
PRODUCT_COPY_FILES += \
    $(COMMON_PATH)/configs/init/fstab.s5e8825:$(TARGET_COPY_OUT_VENDOR)/etc/fstab.s5e8825 \
    $(COMMON_PATH)/configs/init/init.s5e8825.rc:$(TARGET_COPY_OUT_VENDOR)/etc/init/init.s5e8825.rc \
    $(COMMON_PATH)/configs/init/init.s5e8825.usb.rc:$(TARGET_COPY_OUT_VENDOR)/etc/init/init.s5e8825.usb.rc \
    $(COMMON_PATH)/configs/init/init.recovery.s5e8825.rc:$(TARGET_COPY_OUT_RECOVERY)/root/init.recovery.s5e8825.rc \
    $(COMMON_PATH)/configs/init/init.samsung.rc:$(TARGET_COPY_OUT_VENDOR)/etc/init/init.samsung.rc \
    $(COMMON_PATH)/configs/init/ueventd.rc:$(TARGET_COPY_OUT_VENDOR)/etc/ueventd.rc

# Soong namespaces
PRODUCT_SOONG_NAMESPACES += \
    $(LOCAL_PATH)
