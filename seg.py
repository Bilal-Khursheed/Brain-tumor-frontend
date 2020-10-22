

def Read_Chuncks_merge_swap_save(DFKZ_weights, path, path_pre, swapped_axis_path):
    pred_li = []
    i = 3
    for i in range(0, 115):

        volume_val = np.load(path+str(i)+'_.npy')
        pred = DFKZ_weights.predict(volume_val)
        print('--------------')
        print('------Pred--------', pred.shape)
        _classes = pred.argmax(axis=-1)
        print('-------_classes-------', _classes.shape)
        pred_lis.append(_classes)
        print('-------pred_lis-------', len(pred_lis))
        i = i+4
        print("i:", i)
        predictions = np.array(pred_lis)
        print('-------predictions Shape-------', predictions.shape)
        for i in range(0, 35):
            pred_padded_image = np.zeros((256, 256, 155))
            pred_padded_image.shape
            pred_padded_image[0:128, 0:128,
                              13:141] = predictions[i, 0, :, :, :]
            pred_padded_image[0:128, 128:256,
                              13:141] = predictions[i, 2, :, :, :]
            pred_padded_image[128:256, 0:128,
                              13:141] = predictions[i, 1, :, :, :]
            pred_padded_image[128:256, 128:256,
                              13:141] = predictions[i, 3, :, :, :]
            plt.imshow(pred_padded_image[:, :, 76], 'gray')
            plt.show()
            vol1 = vol_names[i]
            vol = str(vol1)

            nib.save(nib.Nifti1Image(pred_padded_image, None),
                     path_pre+vol+'.nii.gz')


def main():
    DFKZ = load_model(
        '/content/drive/My Drive/SLOSH_AI_Solutions_Scripts/Test_Validation_Set/dfkz.h5')
    path = '/content/drive/My Drive/Thesis_Experiments_September_2019/Segmentation_jan_val_chunks/x_data_chunk_128_cube_'
    path_pre = '/content/drive/My Drive/Thesis_Experiments_September_2019/Segmentation_Prediction_Val_35/'
    swapped_axis_path = '/content/drive/My Drive/Thesis_Experiments_September_2019/Segmentation_Swapped_Axis/'
    Read_Chuncks_merge_swap_save(
        DFKZ_weights, path, path_pre, swapped_axis_path)

    #path = sys.argv[1]
    # print(path)
    # stripping(path)
    #print("Working done")


if __name__ == "__main__":
    main()
