class DataAugumentation(object):
    def __init__(self):
        pass

    def image_data_generator(self):
        rotation_data_generator = ImageDataGenerator(
            rotation_range=8,
            width_shift_range=0.1,
            height_shift_range=0.1,
            shear_range=0.2,
            zoom_range=0.2,
            fill_mode='nearest'
        )
        return rotation_data_generator

if __name__ == '__main__':
    image_datagen = my_data_argu.image_data_generator()
    for index in img_labels.index:
        file_name = img_labels.loc[index].values[0]
        file_label = img_labels.loc[index].values[1]
        file_path = img_labels.loc[index].values[2]
        image = load_img(os.path.join(img_input_dir, file_name))
        x = img_to_array(image)
        x = x.reshape((1,) + x.shape)
        aug_amount = arg_num_per_label[file_label]
        print(aug_amount)
        count = 0
        for x_batch in image_datagen.flow(x, batch_size=1):
            count += 1
            if count > aug_amount:
                break
            aug_img = x_batch[0, :, :, 0]
            aug_img_filename = file_name.replace('.', '_gen_%d.' % count)
            cv2.imwrite(os.path.join(img_input_dir, aug_img_filename), aug_img)
            aug_img_labels.append([aug_img_filename, file_label, file_path])
    aug_img_df = pd.DataFrame(aug_img_labels, columns=img_labels.columns)
    all_img_labels = pd.concat([img_labels, aug_img_df], axis=0)
    all_img_labels.sort_values(by='filename').to_excel(os.path.join(img_input_dir, 'aug_label.xlsx'), index=False)

